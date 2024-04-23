from turtle import *
#forward(200)
title("TRIANGLE")
bgcolor("purple")


up()
goto(-150, -100)
fillcolor("yellow")
begin_fill()
down()

##forward(300)
##left(120)
##forward(300)
##left(120)
##forward(300)
##left(120)

for i in range(3):
    forward(300)
    left(120)

end_fill()
hideturtle()
exitonclick()
