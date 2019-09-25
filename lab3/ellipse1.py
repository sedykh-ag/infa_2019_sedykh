from math import*
from graph import *


def ellipse(x, y, a, b, n):
	coordinats_ellips=[]
	for i in range(n):
		coordinats_ellips.append((x+a*cos(2*pi*i/n) , y+b*sin(2*pi*i/n)))
		polygon(coordinats_ellips)

ellipse(50, 330, 40, 30, 10)

run()