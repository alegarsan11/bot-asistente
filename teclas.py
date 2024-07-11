from time import sleep
import pyautogui as bot

def funcion(hacer):
    if hacer == 1:
        bot.keyDown('alt')                
        bot.keyDown('tab')
        bot.keyUp('tab')
        bot.keyUp('alt')
    elif hacer == 2:
        bot.press('win')
        sleep(0.5)
        bot.typewrite('tecl')
        bot.press('enter')
