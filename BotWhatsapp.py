import pyautogui as bot
import webbrowser as web
from time import sleep

def habla(numero):
    web.open("https://web.whatsapp.com/send?phone=+34"+ numero)
    



