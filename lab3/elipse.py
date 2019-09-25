from graph import *
import math as m


penSize(4)
windowSize(1000, 1000)
canvasSize(400, 600)

def zalupa(event):
	print("Координаты: (%s %s)" % (event.x, event.y))

n = 100
a = []
k=1
for i in range(n):
	x = 150
	y = 150
	#point(x+40*m.cos(2*m.pi*i/n), y+100*m.sin(2*m.pi*i/n))
	if i <= (n/4):
		point(x+40*m.cos(2*m.pi*i/n)+k, y+100*m.sin(2*m.pi*i/n))
		k += 3
	else:
		point(x+40*m.cos(2*m.pi*i/n), y+100*m.sin(2*m.pi*i/n))

onMouseDown(zalupa)



run()