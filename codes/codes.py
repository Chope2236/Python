import json
from re import L
from types import CodeType
from typing import ItemsView, Text
from pyzbar import pyzbar
from PIL import Image
import webbrowser
import re

def main():

     json_file = open("C:\\Users\\Chope\\Desktop\\programacion\\Python\\codes\\items.json", "r")
     data = json.load(json_file)
     ch = str(input("Insert qrcode to scan a QR code or barcode to scan a Barcode: "))

     def qrcode():
          qrloc = str(input("Insert the QRCode Image location: "))
          qr = Image.open(qrloc)
          output = pyzbar.decode(qr)
          data = str(output[0].data)
          if 'https://' in data:
           URL = str(re.search("(?P<url>https?://[^\s]+)", data).group("url"))
           webbrowser.open(URL)
          else:
               textfromqr = str(output[0].data, 'utf-8')
               print(textfromqr)

     def barcode():
      bcloc = str(input("Insert the Barcode Image Location:"))
      bc = Image.open(bcloc)
      output = pyzbar.decode(bc)
      barcodenumber = str(output[0].data, "utf-8")
      print(barcodenumber)
      for i in data:
           code = str(i['code'])
           name = i['name']
           if barcodenumber in code:
                print(name)
     

     if 'qrcode' in ch:     
      qrcode()

     elif 'barcode' in ch:
      barcode()

if __name__ == '__main__':
     main()