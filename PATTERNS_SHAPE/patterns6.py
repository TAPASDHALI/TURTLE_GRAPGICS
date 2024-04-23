import turtle as t
t.title("pAtTeRnS")
list = ["yellow", "purple", "blue", "green"]
t.up()
t.goto(240, 0)
for i in range(4):
    t.down()
    t.begin_fill()
    t.fillcolor(list[i])
    t.circle(60)
    t.end_fill()
    t.up()
    t.bk(118.5)
