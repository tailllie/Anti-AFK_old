import pyautogui as pag
from tkinter import *
import random
import time
import threading

duration = 0.2  # duration of cursor movement & pressing key
interval = 10  # interval between cursor movements & pressing key

# New global variable to control key presses
key_press_running = False


def generate_random_coordinates():
    x = random.randint(250, 375)
    y = random.randint(375, 450)
    return x, y


def press_random_key():
    keys = ['w', 'a', 's', 'd']
    pag.press(random.choice(keys))


def run_script():
    while script_running:
        x, y = generate_random_coordinates()
        pag.moveTo(x, y, duration)
        press_random_key()  # press a random key
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


def toggle_key_press():
    global key_press_running
    key_press_running = not key_press_running


# app window
root = Tk()
root.title("SuperPower")
root.geometry("150x80")

# frame for center
center_frame = Frame(root)
center_frame.pack(expand=True, fill="both")

# button to start/stop script
script_running = False
button = Button(center_frame, text="Start", command=toggle_script)
button.pack(pady=5)

# checkbox to toggle key press
key_checkbox = Checkbutton(center_frame, text="Toggle Key Press", command=toggle_key_press)
key_checkbox.pack(pady=5)

root.mainloop()
