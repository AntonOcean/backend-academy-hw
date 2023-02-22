import requests

for i in range(1000000):
    r = requests.get("http://127.0.0.1:8000/hello")

    if r.status_code != 200:
        print("super")
        break
