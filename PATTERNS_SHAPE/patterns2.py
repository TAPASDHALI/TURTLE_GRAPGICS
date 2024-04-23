
def draw_circle(x, y, color, rad):
    t.goto(x, y)
    t.down()
    t.begin_fill()
    t.fillcolor(color)
    t.circle(rad)
    t.end_fill()
    t.up()
    t.home()




import turtle as t
t.up()
draw_circle(0, -50, "green", 60)
draw_circle(200, 200, "purple", 60)
draw_circle(-200, 200, "red", 60)
draw_circle(-200, -200, "yellow", -60)
draw_circle(200, -200, "blue", -60)
