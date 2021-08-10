from os import write
import requests
from requests.models import DEFAULT_REDIRECT_LIMIT

def get_request_and_file():
 r = requests.get(url)
 if r.status_code == 200:
    print("GET request executed succesfully.")
    f = open("html.txt", "w")
    f.write(str(r.text.encode("utf-8")))
    f.close()
 else:
    print("GET request failed.")

def find_string_file():
 f = open("html.txt", "r")
 if strtofind in f.read():
     print("String founded.")
 else:
     print("String not found.")
url = str(input("Insert a complete URL (https:// etc etc): "))
get_request_and_file()
strtofind = str(input('Insert the string that you want to find: '))
find_string_file()

