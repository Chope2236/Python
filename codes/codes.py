from tkinter import font
import PIL
import json
from pyzbar import pyzbar
from PIL import Image
import webbrowser
import re
from tkinter import *
from tkinter import filedialog
window = Tk()
window.title('Codes Scaner')
window.geometry("300x300")

def main():
    json_file = open("C:\\Users\\Chope\\Desktop\\programacion\\Python\\codes\\items.json", "r")
    data = json.load(json_file)
    IMG = PIL.Image
    filename = filedialog.askopenfilename(initialdir = "C:/Users/Desktop",title = "Select a File",filetypes = (("PNG Files","*.png*"),("all files","*.*")))
    imgtsc = PIL.Image.open(filename)
    output = pyzbar.decode(imgtsc)
    datastr = str(output[0].data, 'utf-8')
    if 'https://' in datastr:
        URL = str(re.search("(?P<url>https?://[^\s]+)", datastr).group("url"))
        webbrowser.open(URL)
    else:
        for i in data:
           code = str(i['code'])
           name = i['name']
           if datastr in code:
                itemlbl = Label(window, text=name, font=("Helvetica",12), background="red")
                itemlbl.place(x=10,y=0)

qrcodeimg = PhotoImage(file="C:\\Users\\Chope\\Desktop\\frame2.png")
button_explore = Button(window, image=qrcodeimg, command= main,bd=0, height=256, width=256,bg="white")
button_explore.place(x=20,y=10)

window.config(background="white")
window.mainloop()
