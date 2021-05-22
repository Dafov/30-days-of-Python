import requests

ngrok_url ="https://4b55bd83a807.ngrok.io"
endpoint = f"{ngrok_url}/box-office-mojo-scraper"

r = requests.post(endpoint, json={})
print(r.json()['data'])
