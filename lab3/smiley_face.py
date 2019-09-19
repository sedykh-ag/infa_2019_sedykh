from graph import *

penSize(3)
penColor("black")

brushColor("yellow")
circle(250, 250, 200)

brushColor("red")
circle(170, 180, 40)

brushColor("red")
circle(330, 180, 30)

brushColor("black")
circle(170, 180, 15)

brushColor("black")
circle(330, 180, 8)

rectangle(170, 340, 330, 360)

polygon([(100, 50), (200+40, 120+40), (180+40, 140+40), (80, 70)])

polygon([(300+120, 50+50), (200+70, 100+50), (230+70, 120+50), (340+100, 80+50)])

run()