import turtle
wn=turtle.Screen()
wn.bgcolor("black")
wn.title("sabi lah")
wn.setup(width=400,height=400)
red=turtle.Turtle()

def curve():
    for i in range(200):
        red.right(1)
        red.forward(1)

def heart():
    red.pencolor('pink')
    red.fillcolor('red')
    red.begin_fill()
    red.left(140)
    red.forward(113)
    curve()
    red.left(120)
    curve()
    red.forward(112)
    red.end_fill()
heart()
red.ht()
turtle.done()
