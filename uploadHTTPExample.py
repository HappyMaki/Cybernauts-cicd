import requests

url = "https://34.125.216.208/upload_new_build"

payload={}
files=[
  ('file',('UnityDockerRuntime.zip',open('/S:/UnityProjects/MyProjects/Cybernauts/UnityDockerRuntime/UnityDockerRuntime.zip','rb'),'application/zip'))
]
headers = {
  'token': 'asdasd'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
