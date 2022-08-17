import pywhatkit
import keyboard
import time
from datetime import datetime

contatos = ["+5554999563895","+5554999751888"]

while len(contatos) >= 1:
    pywhatkit.sendwhatmsg(contatos[0],'Maximiliano aki!!!!',datetime.now().hour,datetime.
    now().minute + 2)
    del contatos[0]
    time.sleep(60)
    keyboard.press_and_release('ctrl + w')