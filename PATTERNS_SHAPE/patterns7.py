import turtle as t
t.title("pAtTeRnS")
list = ["yellow", "purple", "blue", "green"]
t.up()
t.goto(240, 0)
for i in range(4):
    t.color(list[i])
    t.pensize(10)
    t.down()
    t.circle(100)
    t.up()
    t.bk(100)
