#!/usr/bin/env python

import pyautogui
import random
import time

screen_width = pyautogui.size().width
screen_height = pyautogui.size().height

original_x = pyautogui.position().x
original_y = pyautogui.position().y
iteration = 1
while True:
    new_x = random.randint(0,screen_width)
    new_y = random.randint(0,screen_height)
    print("{}.Current Position: {}, New Position: x={}, y={}".format(iteration,pyautogui.position(), new_x, new_y))
    pyautogui.moveTo(new_x, new_y)
    iteration+=1
    time.sleep(5)
