from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from pyperclip import paste
import keyboard
import shutil
from pywinauto.timings import Timings
import time
app = Application(backend='uia').connect(path="F:\ImageGlass_Kobe_8.7.11.6_x64\ImageGlass.exe")
Mwindow = app.top_window()
characterOne = r"E:\photograph\one"
characterTwo = r"E:\photograph\two"
characterThree = r"E:\photograph\three"


def q():
    Timings.defaults()
    sourcefile = right()
    print("charcterone    " + sourcefile)
    shutil.move(sourcefile, characterOne)
    print("excute move one    " + str(time.time()))
    print("============================")
    Timings.defaults()

def w():
    Timings.defaults()
    sourcefile = right()
    print("chatacterTwo   " + sourcefile)
    shutil.move(sourcefile, characterTwo)
    print("excute move two      " + str(time.time()))
    print("============================")
    Timings.defaults()

def r():
    Timings.defaults()
    sourcefile = right()
    print("characterThree    " + sourcefile)
    shutil.move(sourcefile, characterThree)
    print("excute move three        " + str(time.time()))
    print("============================")
    Timings.defaults()

def a():
    Timings.defaults()
    send_keys('{DEL}')
    print("delete       " + str(time.time()))
    print("============================")
    Timings.defaults()

def right():
    Timings.defaults()
    send_keys("^l")
    info = paste()
    return info


Mwindow.wait("active")
# send_keys("^l")
# info = paste()
print("start...")
# keyboard.add_hotkey('right', right)
keyboard.add_hotkey('q', q)
keyboard.add_hotkey('w', w)
keyboard.add_hotkey('r', r)
keyboard.add_hotkey('a', a)
# keyboard.add_hotkey('space', right)
keyboard.wait()
