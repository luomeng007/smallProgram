# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/4/13 19:12
software: PyCharm

Description:
    we can set button font and width as well as function
"""
import turtle
import time


def LittleHeart():
    for i in range(200):
        turtle.right(1)
        turtle.forward(2)


love = input('请输入表白语句，然后回车，(例如"I Love You"):\n')
me = input('请输入要表白的人(例如"李思思"):\n')
if love == '':
    love = 'I Love you'
# Set the size and position of the main window.
# 虽然提示找不到对应的函数，但是确实有效，原始文档中也有用法
turtle.setup(width=900, height=600)
turtle.color('red', 'pink')
turtle.pensize(15)
turtle.speed(1000)

turtle.up()

turtle.hideturtle()
turtle.goto(0, -180)
turtle.showturtle()
turtle.down()
turtle.speed(500)
turtle.begin_fill()
turtle.left(140)
turtle.forward(224)
LittleHeart()
turtle.left(120)
LittleHeart()
turtle.forward(224)
turtle.end_fill()
turtle.pensize(12)
turtle.up()
turtle.hideturtle()
turtle.goto(0, -20)
turtle.showturtle()
turtle.color('#CD5C5C', 'pink')
turtle.write(love, font=('gungsuh', 50,), align="center")
turtle.up()
turtle.hideturtle()
if me != '':
    turtle.color('black', 'pink')
    time.sleep(1)
turtle.goto(180, -180)
turtle.showturtle()
turtle.write(me, font=(20, 25), align="center", move=True)
window = turtle.Screen()

# Bind bye() method to mouse clicks on the Screen.
# turtle.bye()
# Shut the turtlegraphics window.
# this command is so cool
window.exitonclick()
