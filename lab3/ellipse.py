from graph import *
import math as m


penSize(4)
windowSize(1000, 1000)
canvasSize(400, 600)
brushColor("black")

def ellipse(x, y, A, B):
	n = 50
	a = []
	for i in range(n):
		a.append((x+A*m.cos(2*m.pi*i/n), y+B*m.sin(2*m.pi*i/n)))
	polygon(a)

ellipse(200, 400, 60, 100)

run()