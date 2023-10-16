import turtle
colors = ["red", "orange", "green", "yellow", "purple", "blue"]
turtle.bgcolor("black")
t=turtle.Turtle()
for x in range(360):    
    t.pencolor(colors[x%6])
    t.forward(x)
    t.left(61)