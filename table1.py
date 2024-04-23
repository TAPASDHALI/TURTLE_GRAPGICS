import turtle as t
t.penup()
x = -200
y = 200
t.goto(x, y)
t.penup()
for i in range(1, 11, 1):
    y = y -30
    for j in range(1, 11, 1):
        t.penup()
        t.speed(1)
        t.forward(20)
        t.write(i * j)
    t.goto(x, y)
