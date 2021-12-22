from tkinter import font
import PIL
import json
from pyzbar import pyzbar
from PIL import Image
import webbrowser
import re
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
window = Tk()
window.title('Codes Scaner')
window.geometry("300x300")
window.resizable(0,0)

def main():
    json_item_file()
    decoding()
    #looks for URL
    if 'https://' in decoding.datastr:
        URL = str(re.search("(?P<url>https?://[^\s]+)", decoding.datastr).group("url"))
        webbrowser.open(URL)
    else:
        #looks for item
        for i in json_item_file.data:
           code = str(i['code'])
           name = i['name']
           if decoding.datastr in code:
               itemlbl = Label(window, text=name, font=("Helvetica",8), background="red")
               itemlbl.place(x=10,y=235)
               itemlbl.pack()
               window.after(3000, itemlbl.destroy)

def json_item_file():
    json_file = open(".\items.json", "r")
    json_item_file.data = json.load(json_file)

def decoding():
    filename = filedialog.askopenfilename(initialdir = "./",title = "Select a File",filetypes = (("PNG Files","*.png*"),("all files","*.*")))
    imgtsc = PIL.Image.open(filename)
    output = pyzbar.decode(imgtsc)
    decoding.datastr = str(output[0].data, 'utf-8')

qrcodeimg = PhotoImage(file=".\\images\\btn_image.png")
button_explore = Button(window, image=qrcodeimg, command= main,bd=0, height=256, width=256,bg="white")
button_explore.place(x=20,y=10)
window.config(background="white")
window.iconbitmap('.\images\ico.ico')
window.mainloop()