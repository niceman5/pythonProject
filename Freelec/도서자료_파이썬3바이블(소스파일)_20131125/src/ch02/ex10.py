# ex10.py
import math
from turtle import *

reset()

t1 = Turtle()
t2 = Turtle()

yamp = 100
rad = 0
y1 = yamp * math.sin(rad)
y2 = yamp * math.cos(rad)
t1.up(); t2.up()
t1.goto(0, y1)
t2.goto(0, y2)
t1.down(); t2.down()
for deg in range(0, 361, 10):
    rad = math.radians(deg)
    y1 = yamp * math.sin(rad)
    y2 = yamp * math.cos(rad)
    t1.goto(rad*50, y1)
    t2.goto(rad*50, y2)

done()
