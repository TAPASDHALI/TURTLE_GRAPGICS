import turtle as t

def petal(t, r, angle):
    """
    Use the turtle(t) to draw a petal using two arcs
    with the radius(r) and angle
    """
    for i in range(2):
        t.circle(r, angle)
        t.left(180-angle)
        
def flower(t, n, r, angle):
    """
    Use the turtle(t) to draw a flower with(n) petals,
    each with the radius(r) and angle.
    """
    for i in range(n):
        petal(t, r, angle)
        t.left(360.0/n)
        
flower(t, 7, 80.0, 60.0)
t.hideturtle()
