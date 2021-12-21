from os import write
import requests
from requests.models import DEFAULT_REDIRECT_LIMIT


def main():
 main.url = str(input("Insert a complete URL (https:// etc etc): "))
 get_request_and_file()
 ask_user()

 
def get_request_and_file():
 r = requests.get(main.url)
 if r.status_code == 200:
    print("GET request executed succesfully.")
    f = open("htmlproject/html.txt", "w")
    f.write(str(r.text.encode("utf-8")))
    f.close()
 else:
    print("GET request failed.")


def find_string_file():
 strtofind = str(input('Write the string that you want to find: '))
 f = open("htmlproject/html.txt", "r")
 if strtofind in f.read():
     print("String found.")
 else:
     print("String not found.")


def ask_user():
 yes = {'yes', 'y'}
 no = {'no', 'n'}
 answer = input('Is there any string that you want to find?(y - n): ')
 if answer in no:
     return 0
 elif answer in yes:
     find_string_file()
 elif answer == '':
     ask_user()

if __name__ == "__main__":
    main()