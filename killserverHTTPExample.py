import requests

url = "https://34.125.216.208/kill_server"

payload={}
headers = {
  'token': 'asdasd'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
