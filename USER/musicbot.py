import screeninfo
import screeninfo as screeninfo
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from screeninfo import get_monitors



print("bot Starting!")

pyautogui.displayMousePosition()

pianoNote = 0

while True:
    screeninfo.get_monitors()[0].width


while True:
    pyautogui.pixel()


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
