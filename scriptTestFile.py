import requests

url = "http://speedtest.tele2.net/10MB.zip"

resp = requests.get(url)

print(resp.status_code)