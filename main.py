# # # # # # # # # #
# autor: NikASGiG #
# # # # # # # # # #

import pyautogui as a
from time import sleep
sleep(7)
def green():
    a.moveTo(53, 75, 0.2)
    a.click()
def red():
    a.moveTo(123, 75, 0.2)
    a.click()
def perple():
    a.moveTo(196, 75, 0.2)
    a.click()
old_num = 1
new_num = 2
replay = 50
play = True
# green = (x=53, y=75) # red = (x=123, y=75) # perple = (x=196, y=75)

while play:
    green()
    sleep(1)
    a.typewrite("Client" + str(old_num))
    sleep(0.2) 
    a.keyDown("Enter")
    a.keyUp("Enter")
    sleep(1)
    perple()
    sleep(1)
    a.typewrite("Client" + str(new_num))
    sleep(0.2)
    a.keyDown("Enter")
    a.keyUp("Enter")
    sleep(4)
    a.keyDown("Enter")
    a.keyUp("Enter")
    red()
    sleep(1)
    print(old_num)
    old_num += 1
    print(old_num)
    new_num += 1
    if old_num >= replay:
        play = False

