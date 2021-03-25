# # # # # # # # # #
# autor: NikASGiG #
# # # # # # # # # #

import pyautogui as a
from time import sleep

# a.moveTo(200, 300, 0.2) # двигает мышь на x и y пикселей, плавно.

# a.drag(50, 50, 0.5, button = "left") # рисует мишью (двигает зажатой) плавно, и в какую сторону

# a.dragTo(200, 300, 1) # плавно тянет мышь от полжения

# a.dragRel(200, 300, 1) # a.moveRel(200, 300, 0.2) # x+x y+y 

# a.position() # x и y настоящего положения мыши

# a.Click(50, 66) # a.leftClick(50, 66) a.rightClick(50, 66) # клик мышью на положение x и y.

# a.alert("massege", "title", button = "button text") # окошко с контентом

# content = a.prompt("bla bla bla", "hapa papa pa") # окно для получения инфы от юзера

# a.confirm("ban exe" ("oooo noooo", "oooo shiiiiit")) # выбор кнопок

# a.password("Enter password", "ooo ban")

# print(a.size()) # расширение экрана

# a.click( clicks = 1, interval = 0.25, button = "left" ) # клик

# a.scroll(1000) # скролить - листать

# a.press("a") # нажать а

# a.typewrite("aaaaa", 0.3) # написать ааааа

# a.keyDown("ctrl") # a.keyDown("s") a.keyUp("ctrl") a.keyUp("s") # зажать и отжать клавиши

# a.hotkey("ctrl", "s") # можно тоже юзать

sleep(3)

# green = (x=53, y=75) # red = (x=123, y=75) # perple = (x=196, y=75)
print(a.position())


input()

