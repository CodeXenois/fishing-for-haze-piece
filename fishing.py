import threading
import pyautogui
import time
from pynput import keyboard

hot_key = keyboard.KeyCode(char="[")
kill_key = keyboard.KeyCode(char="]")

deb = False
program = True
debounce = True
exist = False

def Clicking():
    for x in range(10):
            pyautogui.leftClick()
            print(x)

def FindImage():
    global exist
    if exist is False:
        pyautogui.leftClick()

    time.sleep(1)
    Pole = pyautogui.locateCenterOnScreen("Image\FishLine.png",confidence=0.7)
    if Pole is None:
        print("Pole Dont Exist")
    else:
        exist = True
        print("Pole Exist")
    
    Fish = pyautogui.locateCenterOnScreen("Image\Fish.png",confidence=0.9)
    if Fish is None:
        print("No Image Found")
    else:
        print("Image Found")
        t = threading.Thread(target=Clicking)
        t.start()
        exist = False


def AutoFisher():
    while program:
        time.sleep(0.1)
        while deb:
            FindImage()


start_thread = threading.Thread(target=AutoFisher)
start_thread.start()

def on_press(key):
    if key == hot_key:
        global deb
        if deb == True:
            deb = False
            print("On")
        elif deb == False:
            deb = True
            print("Off")
    elif key == kill_key:
        global program
        program = False
        deb = False
        KL.stop()
            
with keyboard.Listener(on_press=on_press) as KL:
    KL.join()