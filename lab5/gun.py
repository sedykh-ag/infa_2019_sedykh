# coding=utf-8
from random import randrange as rnd, choice
import tkinter as tk
import math
import time


def get_polygon_coords(R, n, x0=300, y0=300):
    vertex = []
    for i in range(n):
        x = x0 + R * math.cos((2 * math.pi * i) / n)
        y = y0 + R * math.sin((2 * math.pi * i) / n)
        vertex.append((x, y))
    return vertex


def tuple_to_array(given):
    array = []
    for pair in given:
        for element in pair:
            array.append(element)

    return array


"""Ball"""


class Ball:
    def __init__(self, storage, x, y):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.storage = storage
        self.x = x
        self.y = y
        self.r = 10
        self.vertexes_count = rnd(3, 7)
        self.vx = 0
        self.vy = 0
        self.gy = -2
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_polygon(get_polygon_coords(
            self.r, self.vertexes_count, self.x, self.y),
                                      fill=self.color)
        self.type = 0  # 0 if created by God, 1 if created by explosion

        self.live = 80

    def set_coords(self):
        vertexes = get_polygon_coords(self.r, self.vertexes_count, self.x,
                                      self.y)
        canv.coords(self.id, tuple_to_array(vertexes))

    def move(self):
        friction_x = 1
        friction_y = 0.5
        self.vy += self.gy
        self.x += self.vx
        self.y -= self.vy

        if self.x + self.r >= 800:
            self.x -= (self.x + self.r) - 800
            self.vx = -self.vx
        elif self.x - self.r <= 0:
            self.x = self.r
            self.vx = -self.vx

        if self.y + self.r >= 500:
            self.y -= (self.y + self.r) - 500
            self.vy = -self.vy * friction_y

            # Трение
            if self.vx > 0:
                self.vx -= friction_x * abs(self.vy)
                if self.vx < 0:
                    self.vx = 0
            elif self.vx < 0:
                self.vx += friction_x * abs(self.vy)
                if self.vx > 0:
                    self.vx = 0

        self.set_coords()

    def hittest(self, obj):
        if math.hypot(self.x - obj.x, self.y - obj.y) <= (self.r + obj.r):
            canv.delete(self.id)
            return True
        else:
            return False

    def explode(self):  # explosion
        canv.delete(self.id)
        n = rnd(2, 7)
        particle_balls = [
            Ball(self.storage, self.x + rnd(5, 10), self.y + rnd(5, 10))
            for _ in range(n)]
        for i in range(n):
            particle_balls[i].type = 1
            particle_balls[i].r = 4
            particle_balls[i].vx = (self.vx / 2) + rnd(-5, 5)
            particle_balls[i].vy = (self.vy / 2) + rnd(-5, 5)
            self.storage.balls += [particle_balls[i]]


"""Gun"""


class Gun:
    def __init__(self, storage):
        self.x = 20
        self.y = 450

        self.storage = storage
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(self.x,
                                   self.y,
                                   self.x + 30,
                                   self.y - 30,
                                   width=7)

    def move(self, x, y):
        self.x += x
        self.y += y
        canv.coords(self.id, self.x, self.y,
                    self.x + max(self.f2_power, 20) * math.cos(self.an),
                    self.y + max(self.f2_power, 20) * math.sin(self.an))
        canv.update()

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        storage.bullet += 1
        new_ball = Ball(self.storage, self.x, self.y)
        new_ball.r += 5
        if event.x < self.x:
            self.an = math.atan(
                (event.y - new_ball.y) / (event.x - new_ball.x))
        elif event.x > self.x:
            self.an = -math.pi + math.atan(
                (event.y - new_ball.y) / (event.x - new_ball.x))

        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = -self.f2_power * math.sin(self.an)

        new_ball.vx = -self.f2_power * math.cos(self.an)
        new_ball.vy = self.f2_power * math.sin(self.an)

        self.an = self.an - math.pi

        storage.balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if event.x > self.x:
                self.an = math.atan((event.y - self.y) / (event.x - self.x))
            elif event.x < self.x:
                self.an = -(math.pi - math.atan(
                    (event.y - self.y) / (event.x - self.x)))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, self.x, self.y,
                    self.x + max(self.f2_power, 20) * math.cos(self.an),
                    self.y + max(self.f2_power, 20) * math.sin(self.an))

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


"""Target"""


class Target:
    def __init__(self, storage):
        self.vx = 0
        self.vy = 0
        self.storage = storage
        self.storage.points = 0
        self.live = 1
        self.x = 0
        self.y = 0
        self.r = 1
        self.vertexes_count = rnd(3, 7)
        self.vertexes = None
        self.color = 'red'

        self.id = canv.create_polygon(get_polygon_coords(
            self.r, self.vertexes_count, self.x, self.y),
                                      fill=self.color)

        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = rnd(400, 780)
        self.y = rnd(100, 400)
        self.vx = rnd(-5, 5)
        self.vy = rnd(-5, 5)
        self.r = rnd(20, 30)
        self.vertexes_count = rnd(3, 7)
        self.vertexes = get_polygon_coords(self.r, self.vertexes_count, self.x,
                                           self.y)
        self.vertexes = tuple_to_array(self.vertexes)
        canv.coords(self.id, self.vertexes)
        canv.itemconfig(self.id, fill=self.color)

    def remove(self):
        self.x = 10
        self.y = -10
        self.r = 0
        canv.coords(self.id, -10, -10, -10, -10)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        self.x = 10
        self.y = -10
        self.r = 0
        self.storage.points += points
        canv.itemconfig(self.storage.id_points, text=self.storage.points)

    def move(self):
        """Движение мишени"""
        if self.vx != 0 or self.vy != 0:
            """Проверка выхода за границу x"""
            if self.x + self.r >= 800:
                self.x -= (self.x + self.r) - 800
                self.vx = -self.vx
            elif self.x - self.r <= 0:
                self.x = self.r
                self.vx = -self.vx
            """Проверка выхода за границу y"""
            if self.y + self.r >= 500:
                self.y -= (self.y + self.r) - 500
                self.vy = -self.vy
            elif self.y - self.r <= 0:
                self.y = self.r
                self.vy = -self.vy

            self.x += self.vx
            self.y += self.vy
            vertexes = canv.coords(self.id)
            for i in range(len(vertexes)):
                if i % 2 == 0:
                    vertexes[i] = vertexes[i] + self.vx
                else:
                    vertexes[i] = vertexes[i] + self.vy
            canv.coords(self.id, vertexes)
            canv.update()


"""Storage"""


class Storage:
    def __init__(self):
        self.screen1 = canv.create_text(400, 300, text='', font='28')
        self.g1 = None
        self.bullet = 0
        self.balls = []
        self.targets = []
        self.points = 0
        self.id_points = canv.create_text(30, 30, text=self.points, font='28')


def new_game(storage, event=''):
    for b in storage.balls:
        canv.delete(b.id)
    canv.update()
    storage.balls = []
    storage.bullet = 0
    for t1 in storage.targets:
        t1.new_target()
    canv.bind('<Button-1>', storage.g1.fire2_start)
    canv.bind('<ButtonRelease-1>', storage.g1.fire2_end)
    canv.bind('<Motion>', storage.g1.targetting)
    root.bind('<w>', lambda event: storage.g1.move(0, -10))
    root.bind('<s>', lambda event: storage.g1.move(0, 10))
    root.bind('<a>', lambda event: storage.g1.move(-10, 0))
    root.bind('<d>', lambda event: storage.g1.move(10, 0))

    storage.g1.x = 20
    storage.g1.y = 450

    counter = 0
    z = 0.03
    for t1 in storage.targets:
        t1.live = 1
    while storage.targets[0].live or storage.targets[1].live\
            or storage.targets[2].live:

        for t in storage.targets:
            t.move()

        for b in storage.balls:
            b.move()
            b.live -= 1
            if b.live == 60 and b.type == 0:
                b.explode()

            if b.live <= 0:
                canv.delete(b.id)
                storage.balls.remove(b)

            for t in storage.targets:
                if b.hittest(t) and t.live:
                    b.live = 0
                    canv.update()
                    t.hit()
                    t.live = 0
                    t.remove()
                    counter += 1

            if counter == 3:
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(storage.screen1,
                                text='Вы уничтожили цели за ' +
                                str(storage.bullet) + ' выстрелов')
                canv.update()
                time.sleep(2)

        canv.update()
        time.sleep(z)
        storage.g1.targetting()
        storage.g1.power_up()

    canv.itemconfig(storage.screen1, text='')
    canv.update()
    new_game(storage)


"""Main sequence"""

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)

storage = Storage()  # initialization
storage.g1 = Gun(storage)
target1 = Target(storage)
target2 = Target(storage)
target3 = Target(storage)
storage.targets.append(target1)
storage.targets.append(target2)
storage.targets.append(target3)

new_game(storage)

tk.mainloop()
