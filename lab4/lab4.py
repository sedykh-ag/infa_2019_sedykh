import tkinter as tk
from random import randrange as rnd, choice
import time

root = tk.Tk()
# geomerty(width x height)
root.geometry('800x600')

canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)

colors = ['red', 'orange', 'yellow', 'green', 'blue']
shapes = ['oval']


class Shape:
    def __init__(self, canvas, color, shape):
        self.canvas = canvas
        self.shape = shape
        self.color = color
        self.x = rnd(100, 700)
        self.y = rnd(100, 500)
        self.r = rnd(30, 50)
        self.score = self.r
        self.obj = None

    def draw(self):
        self.obj = self.canvas.create_oval(self.x - self.r, self.y - self.r,
                                self.x + self.r, self.y + self.r,
                                fill=self.color, width=0)

    def move(self):
        root.after(30, self.move)
        self.canvas.delete(self.obj)
        self.x = self.x + 5
        self.draw()


def new_shape():
    shape = Shape(canv, choice(colors), choice(shapes))
    #shape.draw()
    shape.move()
    root.after(1000, new_shape)


def click(event):
    print('click')


new_shape()
canv.bind('<Button-1>', click)
tk.mainloop()
