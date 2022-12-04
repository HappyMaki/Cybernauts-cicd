apt-get update
apt-get install python3-pip
sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose -v
alias docker-compose=/usr/local/bin/docker-compose

python3 -m pip install -r requirements.txt
sudo python3 -u main.py



