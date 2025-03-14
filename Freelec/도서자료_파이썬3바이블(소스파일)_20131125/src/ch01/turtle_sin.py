import turtle
import math

t1 = turtle.Turtle()
turtle.tracer(False)
screen = t1.getscreen()
screen.setworldcoordinates(0, -1.1, 2*math.pi, 1.1)

for deg in range(0, 361, 10):
    rad = math.radians(deg)
    t1.goto(rad, math.sin(rad))

turtle.tracer(True)
turtle.hideturtle()
t1.hideturtle()
turtle.done()
