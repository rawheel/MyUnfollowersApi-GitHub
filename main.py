import requests

BASE = "http://127.0.0.1:500/"

response = requests.get(BASE+"GithubFollowers/wajahatkarim3")
print(response.json())

