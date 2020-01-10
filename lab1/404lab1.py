import requests

print(requests.__version__)

google = requests.get("https://www.google.com")

print(google)

var = requests.get("https://raw.githubusercontent.com/yw4/cmput-404-labs/master/lab1/404lab1.py")

print(var.content)
