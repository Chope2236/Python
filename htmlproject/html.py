from os import write
import requests
from requests.models import DEFAULT_REDIRECT_LIMIT

def main():
 main.url = str(input("Insert a complete URL (https:// etc etc): "))
 get_request_and_file()
 main.strtofind = str(input('Insert the string that you want to find: '))
 find_string_file()

def get_request_and_file():
 r = requests.get(main.url)
 if r.status_code == 200:
    print("GET request executed succesfully.")
    f = open("html.txt", "w")
    f.write(str(r.text.encode("utf-8")))
    f.close()
 else:
    print("GET request failed.")

def find_string_file():
 f = open("html.txt", "r")
 if main.strtofind in f.read():
     print("String found.")
 else:
     print("String not found.")

if __name__ == "__main__":
    main()


