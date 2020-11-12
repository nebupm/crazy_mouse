#!/usr/bin/env python

#============================================================================#
#  This program will keep your mouse on the move. Its usually good when you  #
#  dont want your annoying screensaver to kick in and lock you out while you #
#  were out preparing your coffee.                                           #
#  Copyright (C) 2020  Nebu Mathews                                          #
#                                                                            #
#  This program is free software: you can redistribute it and/or modify      #
#  it under the terms of the GNU General Public License as published by      #
#  the Free Software Foundation, either version 3 of the License, or         #
#  (at your option) any later version.                                       #
#  This program is distributed in the hope that it will be useful,           #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of            #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
#  GNU General Public License for more details.                              #
#                                                                            #
#  You should have received a copy of the GNU General Public License         #
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.    #
#============================================================================#

import pyautogui
import random
import time

screen_width = int(pyautogui.size().width/2)
screen_height = int(pyautogui.size().height/2)

original_x = pyautogui.position().x
original_y = pyautogui.position().y
iteration = 1
print("{}.Current Position: {}, New Position: x={}, y={}".format(
            iteration, pyautogui.position(), original_x, original_y))
try:
    while True:
        new_x = random.randint(screen_width, screen_width+10)
        new_y = random.randint(screen_height, screen_height+10)
        pyautogui.moveTo(new_x, new_y)
        iteration += 1
        print("{}.Current Position: {}, New Position: x={}, y={}".format(
            iteration, pyautogui.position(), new_x, new_y))
        time.sleep(5)
except KeyboardInterrupt:
    print("{}.Current Position: {}, New Position: x={}, y={}".format(
            iteration, pyautogui.position(), original_x, original_y))
    pyautogui.moveTo(original_x, original_y)
    exit(0)
