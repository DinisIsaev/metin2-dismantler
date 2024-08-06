import win32api
import win32con
import cv2
import numpy as np
import time
import pydirectinput
from mss import mss

time.sleep(5)
inventory_box = {'top': 725, 'left': 1750, 'width': 165, 'height': 290}
hasItems = True
item_template = cv2.imread("faca.png")
item_template = cv2.cvtColor(np.array(item_template), cv2.COLOR_BGR2RGB)
sct = mss()
inventory_rec = sct.grab(inventory_box)
inventory_rec = cv2.cvtColor(np.array(inventory_rec), cv2.COLOR_BGR2RGB)
res = cv2.matchTemplate(inventory_rec, item_template, cv2.TM_CCOEFF_NORMED)
if np.any(res > 0.9):
    item_location = np.where( res >= 0.9)
    for item in (zip(*item_location)):
        time.sleep(0.1)
        win32api.SetCursorPos((item[1]+1755, item[0]+740))
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(0.1)
        win32api.SetCursorPos((990,480))
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(0.5)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(0.5)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)