#Program that makes colorful spiral shape
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
screen.colormode(255)

R = 0
G = 0
B = 255

screen.bgcolor((255, 160, 60))

turtle.speed(1000)

colors = []

while R < 255:
    colors.append((R, G, B))
    R += 5
while G < 255:
    colors.append((R, G, B))
    G += 51
while B > 0:
    colors.append((R, G, B))
    B -= 5
while R > 0:
    colors.append((R, G, B))
    R -= 5
while G > 0:
    colors.append((R, G, B))
    G -= 51
  
for i in range(3000):
    turtle.color(colors[i%len(colors)])
    for n in range(4):
        turtle.forward(i/2)
        turtle.right(90)
    turtle.right(85)
