import pyautogui as pag
import random
import time

while True:
    x = random.randint(200,500)
    y = random.randint(300,600)
    pag.moveTo(x,y,0.5)
    time.sleep(2)
