from graph import *
brushColor("black")
penSize(0)
windowSize(1000, 1000)
canvasSize(400, 600)

rectangle(0,0,400,600)

brushColor(128, 102 , 0)
rectangle(0, 300, 400, 600)

brushColor(85, 68 , 0)
rectangle(0, 0, 400, 300)

brushColor(213, 255, 230)
rectangle(215, 10, 390, 290)
#parts of window

brushColor(135, 205, 222)
rectangle(215+10, 10+10, 390-95, 290-140)
rectangle(215+10+85, 10+10, 390-95+85, 290-140)
rectangle(215+10, 10+10+140, 390-95, 290-140+130)
rectangle(215+10+85, 10+10+140, 390-95+85, 290-140+130)


run()