from graph import *
from math import *

brushColor("black")
penSize(5)
windowSize(1000, 1000)
canvasSize(400, 600)

points = []

for t in range(1, 6200, 1):
	a=100
	b=40
	x = (a*cos((2*pi)/(6200-t))+100)
	y = (b*sin((2*pi)/(6200-t))+100)
	point(x,y)

run()