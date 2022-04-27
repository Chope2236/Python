from win10toast import ToastNotifier
import keyboard
from bs4 import BeautifulSoup
import requests
import time
import win32gui, win32con

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def weather(city):
    city = city.replace(" ", "+")
    res = requests.get(
        f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    weather.location = soup.select('#wob_loc')[0].getText().strip()
    weather.info = soup.select('#wob_dc')[0].getText().strip()
    weather.temperature = soup.select('#wob_tm')[0].getText().strip()

toaster = ToastNotifier()
def main():
    city = input("Enter the Name of your city: ")
    the_program_to_hide = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)
    city = city+" weather"
    weather(city)
    temperature = str(weather.temperature + "°C - " + weather.info)
    path = "C:\\Users\\Chope\\Desktop\\Nueva carpeta (2)\\ico.ico" 
    toaster.show_toast(weather.location,temperature,icon_path=path,duration=2.5)
    toaster.show_toast('The app is hidden.','Ctrl + Shift to check the weather.',icon_path=path,duration=2.5,threaded=True)
    while toaster.notification_active(): time.sleep(0.1)
    while True:
        keyboard.wait('ctrl+shift')
        toaster.show_toast(weather.location,temperature,icon_path=path,duration=2.5)
if __name__ == '__main__':
    main()
