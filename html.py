from os import write
import requests

url = str(input("Insert a complete URL (https:// etc etc): "))
r = requests.get(url)
f = open("html.txt", "w")
f.write(str(r.text.encode("utf-8")))

