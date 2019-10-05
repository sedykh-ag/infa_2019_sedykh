from graph import *
import math as m


def ellipse(x0, y0, A, B, angle, size):
    n = 80
    a = []

    for i in range(n):
        x = x0 + A * m.cos(2 * m.pi * i / n) * size
        y = y0 + B * m.sin(2 * m.pi * i / n) * size

        x1 = x0 + (x - x0) * m.cos(angle) - (y - y0) * m.sin(angle)
        y1 = y0 + (y - y0) * m.cos(angle) + (x - x0) * m.sin(angle)

        a.append((x1, y1))

    result = polygon(a)
    return result


penSize(0)
windowSize(700, 1000)
canvasSize(700, 1000)
brushColor("black")

"""Background"""
brushColor("#7F6601")
rectangle(0, 500, 700, 1000)

brushColor("#554400")
rectangle(0, 0, 700, 500)

"""Window"""


def window(x0, y0, size):
    # x0, y0 are top left corner coordinates

    """back"""
    brushColor("#D1FFEB")
    rectangle(x0, y0, x0 + 320 * size, y0 + 450 * size)

    """front"""
    brushColor("#87CDDE")
    rectangle(x0 + 20 * size, y0 + 20 * size, x0 + 150 * size, y0 + 220 * size)

    brushColor("#87CDDE")
    rectangle(x0 + 170 * size, y0 + 20 * size, x0 + 300 * size, y0 + 220 * size)

    rectangle_1 = rectangle(x0 + 20 * size, y0 + 20 * size, x0 + 150 * size, y0 + 220 * size)
    moveObjectBy(rectangle_1, 0, 220 * size)

    rectangle_2 = rectangle(x0 + 170 * size, y0 + 20 * size, x0 + 300 * size, y0 + 220 * size)
    moveObjectBy(rectangle_2, 0, 220 * size)


"""Cat"""


def cat(x0, y0, size):
    """Body"""
    brushColor("#C87137")
    ellipse(x0, y0, 250 * size, 115 * size, 0, size)

    """Head"""
    brushColor("#C87137")
    ellipse(x0 - 230 * size, y0 - 20 * size, 80, 80, 0, size)

    """Nose"""
    polygon([(x0 - 220 * size, y0 + 10 * size), (x0 - 240 * size, y0 + 10 * size), (x0 - 230 * size, y0 + 20 * size)])
    penSize(2)
    penColor("black")
    line(x0 - 230 * size, y0 + 20 * size, x0 - 230 * size, y0 + 40 * size)
    polyline([(x0 - 230 * size, y0 + 40 * size), (x0 - 229 * size, y0 + 41 * size), (x0 - 229 * size, y0 + 42 * size),
              (x0 - 228 * size, y0 + 41 * size), (x0 - 227 * size, y0 + 42 * size), (x0 - 220 * size, y0 + 42 * size),
              (x0 - 217 * size, y0 + 40 * size), (x0 - 214 * size, y0 + 37 * size), (x0 - 214 * size, y0 + 33 * size)])
    polyline([(x0 - 230 * size, y0 + 40 * size), (x0 - 231 * size, y0 + 41 * size), (x0 - 231 * size, y0 + 42 * size),
              (x0 - 232 * size, y0 + 41 * size), (x0 - 233 * size, y0 + 42 * size), (x0 - 240 * size, y0 + 42 * size),
              (x0 - 243 * size, y0 + 40 * size), (x0 - 246 * size, y0 + 37 * size), (x0 - 246 * size, y0 + 33 * size)])


brushColor("#C87137")
ellipse(676, 711 + 20, 150, 40, m.pi / 8, 1)
ellipse(82, 731, 30, 60, 0, 1)

# ellipse(200, 400, 60, 100, m.pi/4, 1)
window(360, 20, 1)
cat(340, 700, 1)

"""Ears"""
penSize(0)
brushColor("#C87137")
right_ear_dark = polygon([(131, 616), (171, 633), (185, 555)])
left_ear_dark = polygon([(50, 643), (84, 615), (21, 565)])
brushColor("#DEAA87")
right_ear_light = polygon([(139, 614), (168, 625), (178, 570)])
left_ear_light = polygon([(54, 634), (76, 613), (28, 577)])

brushColor("#C87137")
penSize(0)
ellipse(519, 741 + 15, 70, 70, 0, 1)
ellipse(598 - 27, 817, 30, 70, 0, 1)
ellipse(181, 782, 70, 25, 0, 1)

"""Mustache right"""
penSize(2)
penColor("black")
polyline([(129, 719), (139, 714), (157, 705), (178, 700), (194, 704), (205, 709)])
polyline([(132, 725), (146, 718), (165, 710), (184, 710), (194, 711), (199, 715), (209, 720), (211, 722)])
polyline([(129, 719 + 17), (139, 714 + 17), (157, 705 + 17), (178, 700 + 17), (194, 704 + 17), (205, 709 + 17)])

"""Mustache left"""
polyline([(89, 716 + 5), (87, 711 + 5), (83, 708 + 5), (78, 704 + 5), (69, 703 + 5), (60, 701 + 5), (49, 701 + 5),
          (40, 701 + 5), (34, 705 + 5), (25, 709 + 5), (21, 712 + 5), (22, 715 + 5)])
polyline([(84, 726), (81, 722), (77, 718), (62, 715), (53, 715), (42, 716), (36, 719), (30, 723), (26, 727), (22, 730),
          (21, 734)])
polyline([(89, 716 + 5 + 17), (87, 711 + 5 + 17), (83, 708 + 5 + 17), (78, 704 + 5 + 17), (69, 703 + 5 + 17),
          (60, 701 + 5 + 17), (49, 701 + 5 + 17), (40, 701 + 5 + 17), (34, 705 + 5 + 17), (25, 709 + 5 + 17),
          (21, 712 + 5 + 17), (22, 715 + 5 + 17)])

"""Eyes"""
penSize(0)
brushColor("#88AA00")
ellipse(144, 667, 25, 25, 0, 1)  # right eyelid
ellipse(77, 667, 25, 25, 0, 1)  # left eyelid

brushColor("black")
right_pupil = ellipse(144 + 7, 667, 3, 21, 0, 1)  # right pupil
left_pupil = ellipse(77 + 7, 667, 3, 21, 0, 1)  # left pupil

"""Hairball"""
brushColor("grey")
ellipse(463, 927, 70, 70, 0, 1)
# lines on hairball
brushColor("black")
polyline([(459, 876), (469, 876), (481, 879), (488, 882), (493, 890), (494, 895), (503, 904), (504, 907), (511, 915),
          (514, 917), (521, 920), (522, 919)])
polyline([(462, 892), (466, 893), (475, 899), (483, 906), (485, 909), (489, 928), (490, 929), (497, 933), (503, 935),
          (505, 937), (525, 942)])
polyline([(430, 885), (438, 885), (442, 889), (445, 892), (448, 899), (453, 908), (455, 913), (460, 925), (464, 935),
          (474, 939), (476, 940), (484, 945), (491, 947), (506, 949), (511, 949), (518, 947)])
polyline([(426, 916), (431, 920), (446, 928), (456, 939), (462, 953), (462, 958), (463, 965), (463, 965), (465, 976)])
polyline([(475, 966), (487, 969), (494, 964), (500, 958)])
penSize(2)
polyline([(199, 974), (203, 970), (213, 954), (226, 939), (239, 935), (294, 931), (308, 936), (315, 942), (325, 950),
          (342, 973), (354, 979), (364, 979), (375, 979), (388, 977), (398, 965), (402, 962)])

"""Animations"""
flag_eyes = True
counter = 1


def eyes_move():
    global flag_eyes

    if flag_eyes:
        moveObjectBy(left_pupil, 0.1, 0)
        moveObjectBy(right_pupil, 0.1, 0)
        if xCoord(right_pupil) > 154:
            flag_eyes = False
    elif not flag_eyes:
        moveObjectBy(left_pupil, -0.1, 0)
        moveObjectBy(right_pupil, -0.1, 0)
        if xCoord(right_pupil) < 128:
            flag_eyes = True


def ears_move():
    global counter
    global right_ear_dark
    global right_ear_light
    global left_ear_dark
    global left_ear_light

    brushColor("#C87137")
    right_ear_dark = polygon([(131, 616), (171, 633), (185 - 21, 555)])
    brushColor("#DEAA87")
    right_ear_light = polygon([(139, 614), (168, 625), (178 - 21, 570)])
    brushColor("#C87137")
    left_ear_dark = polygon([(50, 643), (84, 615), (21 + 21, 565)])
    brushColor("#DEAA87")
    left_ear_light = polygon([(54, 634), (76, 613), (28 + 21, 577)])

    if counter >= 1:
        deleteObject(right_ear_dark)
        deleteObject(right_ear_light)

        brushColor("#C87137")
        right_ear_dark = polygon([(131, 616), (171, 633), (185 - 21 + counter, 555)])
        brushColor("#DEAA87")
        right_ear_light = polygon([(139, 614), (168, 625), (178 - 21 + counter, 570)])
        brushColor("#C87137")
        left_ear_dark = polygon([(50, 643), (84, 615), (21 + 21 - counter, 565)])
        brushColor("#DEAA87")
        left_ear_light = polygon([(54, 634), (76, 613), (28 + 21 - counter, 577)])

        counter += 1

        if counter > 21:
            counter = -1

    elif counter <= -1:

        deleteObject(right_ear_dark)
        deleteObject(right_ear_light)

        brushColor("#C87137")
        right_ear_dark = polygon([(131, 616), (171, 633), (185 + counter, 555)])
        brushColor("#DEAA87")
        right_ear_light = polygon([(139, 614), (168, 625), (178 + counter, 570)])
        brushColor("#C87137")
        left_ear_dark = polygon([(50, 643), (84, 615), (21 - counter, 565)])
        brushColor("#DEAA87")
        left_ear_light = polygon([(54, 634), (76, 613), (28 - counter, 577)])

        counter -= 1
        if counter < -21:
            counter = 1


onTimer(eyes_move, 10)
onTimer(ears_move, 50)

run()
