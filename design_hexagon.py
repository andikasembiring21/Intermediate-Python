import turtle
colors=["red","purple","blue","green","orange","yellow"]
t=turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
for x in range(460):
    t.pencolor(colors[x%6])
    t.width(x//100+1)
    t.forward(x)
    t.left(59)