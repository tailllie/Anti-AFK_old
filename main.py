import pyautogui as pag
from tkinter import *
import random
import time
import threading


duration = 0.2 # duration of cursor movement
interval = 10 # interval between cursor movements


def run_script():
    while script_running:
        x = random.randint(250, 375)
        y = random.randint(375, 450)
        pag.moveTo(x, y, duration)
        time.sleep(interval)

def toggle_script():
    global script_running
    script_running = not script_running
    if script_running:
        button.config(text="Stop")
        # start script on other thread
        script_thread = threading.Thread(target=run_script)
        script_thread.start()
    else:
        button.config(text="Start")

# app window
root = Tk()
root.title("SuperPower")
root.geometry("100x50")

# frame for center
center_frame = Frame(root)
center_frame.pack(expand=True, fill="both")

# button
script_running = False
button = Button(center_frame, text="Start", command=toggle_script)
button.pack(pady=15)

root.mainloop()
