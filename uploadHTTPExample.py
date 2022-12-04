import requests

url = "https://34.125.63.136"

payload={}
files=[
  ('file',('UnityDockerRuntime.zip',open('/S:/UnityProjects/MyProjects/Cybernauts/UnityDockerRuntime/UnityDockerRuntime.zip','rb'),'application/zip'))
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
