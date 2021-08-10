from os import write
import requests
from requests.models import DEFAULT_REDIRECT_LIMIT

def get_request_and_file():
 r = requests.get(url)
 if r.status_code == 200:
    print("GET request executed succesfully.")
    f = open("html.txt", "w")
    f.write(str(r.text.encode("utf-8")))
 else:
    print("GET request failed.")

url = str(input("Insert a complete URL (https:// etc etc): "))
get_request_and_file()

