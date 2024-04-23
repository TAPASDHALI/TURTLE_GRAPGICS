Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
turtle.pendown()
turtle.fillcolor("purple")
turtle.begin_fill()
turtle.circle()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    turtle.circle()
TypeError: circle() missing 1 required positional argument: 'radius'
turtle.circle(70)
turtle.end_fill()
turtle.penup()
turtle.goto(-25, 50)
turtle.hideturtle()
turtle.write('Circle!', font = ('Times New Roman', 20, 'bold'))
turtle.title("Circle!")
