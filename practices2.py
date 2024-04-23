Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
t = turtle.Turtle()
t.color("red")
t.shape("turtle")
t.color("blue")
wn = turtle.screen()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    wn = turtle.screen()
AttributeError: module 'turtle' has no attribute 'screen'. Did you mean: 'Screen'?
KeyboardInterrupt
wn = turtle.Screen()
wn.bgcolor("purple")
wn.bgcolor("black")
turtle.colormode()
1.0
turtle.colormode(255)
wn.bgcolor()
'black'
wn.bgcolor(170,30,20)
wn.bgcolor("purple")
wn = turtle.Screen()
wn.bgpic("python 