import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import shutil
import zipfile
import subprocess

TOKEN = "asdasd"
UPLOAD_FOLDER = 'upload_dir'
ALLOWED_EXTENSIONS = {'zip', 'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/kill_server")
def killserver():
    token = request.headers.get('token')
    if token != TOKEN:
        return "failed token check"
    command = "cd server_build;sudo docker-compose down"
    result = subprocess.run(command, shell=True)
    return str(result.returncode)

@app.route("/start_server")
def startserver():
    token = request.headers.get('token')
    if token != TOKEN:
        return "failed token check"
    command = "cd server_build;sudo docker-compose build;sudo docker-compose up &"
    result = subprocess.run(command, shell=True)
    return str(result.returncode)

def DeleteAllFilesInDirection(dirpath):
    directory = dirpath

    # List the contents of the directory
    for item in os.listdir(directory):
        # Construct the full path to the item
        item_path = os.path.join(directory, item)

        # Check if the item is a file or a directory
        if os.path.isfile(item_path):
            # Delete the file
            os.remove(item_path)
        elif os.path.isdir(item_path):
            # Delete the directory and its contents
            shutil.rmtree(item_path)

def UnzipTheFile(zip_file):
    # Replace this with the path to the directory where you want to save the unzipped files
    output_directory = 'server_build'

    # Open the zip file
    with zipfile.ZipFile(UPLOAD_FOLDER + "/" + zip_file, 'r') as z:
        # Extract the files to the output directory
        z.extractall(output_directory)

@app.route('/upload_new_build', methods=['GET', 'POST'])
def upload_file():
    token = request.headers.get('token')
    if token != TOKEN:
        return "failed token check"
    if request.method == 'POST':
        DeleteAllFilesInDirection(UPLOAD_FOLDER)
        DeleteAllFilesInDirection("server_build")
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            UnzipTheFile(filename)
            return "file accepted"
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=443, ssl_context='adhoc')
    # app.run(host="0.0.0.0", port=80)

