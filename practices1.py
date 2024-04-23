Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
turtle.showturtle()
turtle.circle(45)
turtle.color("red")
turtle.circle(60)
turtle.penup(5)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    turtle.penup(5)
TypeError: penup() takes 0 positional arguments but 1 was given

import turtle

turtle.color('red")
             
SyntaxError: unterminated string literal (detected at line 1)
turtle.color("red")
             
turtle.bgcolor("pink")
             
turtle.circle(60)
             
turtle.circle(70)
             
