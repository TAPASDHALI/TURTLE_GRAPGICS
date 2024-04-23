Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
def square(side):
    for i in range(4):
        turtle.forward(side)
        turtle.left(90)

square(20)
squate(30)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    squate(30)
NameError: name 'squate' is not defined. Did you mean: 'square'?
square(30)
square(40)
square(50)
### CREATE A FUNCTION TO DROW FOUR DIFFERENT SQUARES