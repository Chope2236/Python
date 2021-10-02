import math
import json

def main():
    json_file = open("C:\\Users\\Chope\\Desktop\\programacion\\Python\\codes\\items.json", "r")
    data = json.load(json_file)

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


if __name__ == '__main__':
     main()