import turtle as t
import random

color_list = [(26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227), (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72), (4, 162, 86), (98, 51, 36), (24, 155, 210), (229, 168, 185), (173, 185, 221), (29, 90, 95), (233, 173, 162), (156, 212, 190), (87, 46, 33), (37, 45, 83)]

pad = t.Turtle()
t.colormode(255)
screen = t.Screen()
screen.setup (800, 600, 1000, 400)
# screen.reset()
# screen.setworldcoordinates(-200,-200,200,200)
screen.bgcolor("green")
pad.speed("fastest")
pad.hideturtle()
#create a 10 * 10 dotted picture

width = 400
height = 400

def random_color():
    return random.choice(color_list)

#Setting
def painting_dots(dots, dotstrengh ):
    startx = int(width / 2 * -1)
    starty = int(height/2*-1)
    increasex = int(width / dots)
    increasey = int(height/dots)
    pad.penup()
    for _ in range(dots):
        pad.goto(startx, starty)
        for _ in range(dots):
            pad.goto(startx, starty)
            pad.dot(dotstrengh, random_color())
            startx += increasex
        starty += increasey    
        startx = int(width/2*-1)

painting_dots(15, 20)


screen.exitonclick()