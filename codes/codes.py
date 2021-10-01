import math
import json

def main():
    barcode = str(input("Insert the Bar Code (EAN 13) : "))
    while len(barcode) > 13:
        print("ERROR, Bar code length cant be higher than 13")
        barcode = str(input("Insert the Bar Code (EAN 13) : "))
    json_file = open("C:\\Users\\Chope\\Desktop\\programacion\\Python\\codes\\items.json", "r")
    data = json.load(json_file)
    for i in data:
        code = str(i['code'])
        name = i['name']
        items = code + " - " + name
        if barcode in code:
            print(name)
        elif 'all' in barcode:
            print(items)

#def brcinpt():
    #brcinpt = bar code input
#    brcinpt.barcode = int(input("Insert the Bar Code (EAN 13) : "))
#    while math.log10(brcinpt.barcode) > 13:
#     print("ERROR, Bar code length cant be higher than 13")
#     brcinpt.barcode = int(input("Insert the Bar Code (EAN 13) : ")) 

if __name__ == '__main__':
     main()