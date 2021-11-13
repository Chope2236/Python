import json
from pyzbar import pyzbar
from PIL import Image

def main():

     json_file = open("C:\\Users\\Chope\\Desktop\\programacion\\Python\\codes\\items.json", "r")
     data = json.load(json_file)
     ch = str(input("Insert qrcode to scan a QR code or barcode to scan a Barcode: "))

     if 'qrcode' in ch:
          qr = Image.open('C:/Users/Chope/Desktop/qrcode.jpg')
          output = pyzbar.decode(qr)
          data = output[0].data
          print(data)
          return 0

     elif 'barcode' in ch:
          barcode = str(input("Insert the Bar Code (EAN 13) : "))
     while len(barcode) > 13:
        print("ERROR, Bar code length cant be higher than 13")
        barcode = str(input("Insert the Bar Code (EAN 13) : "))

     for i in data:
      code = str(i['code'])
     name = i['name']
     items = code + " - " + name

     if barcode in code:
        print(name)
     elif 'all' in barcode:
        print(items)
     
     return 0
if __name__ == '__main__':
     main()