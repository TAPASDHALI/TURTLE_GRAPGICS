import turtle as t
t.title("pAtTeRnS")
list1 = ["yellow", "purple", "blue", "green", "red"]
for i in range(200):
    t.color(list1[i%5])
    t.pensize(i/10+1)
    t.forward(i)
    t.left(59)
