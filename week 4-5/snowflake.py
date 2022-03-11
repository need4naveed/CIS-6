#Program that creates snowflakes with random colors and sizes
import turtle
import random

bob = turtle.Turtle() #our turtle is named bob
turtle.colormode(255)
turtle.Screen().bgcolor(100,100,100)

bob.penup()
bob.goto(random.randint(-200,0),random.randint(0,200)) #random starting pos
bob.pendown()

def branch(size):          
    bob.forward(size*10) #make the snowflake extra long
    bob.right(30)
    for i in range(3):      #Draws traingles at the tips of snowflakes
        bob.forward(size*2)
        bob.left(120)
    bob.left(30)
    for i in range(3):
        bob.backward(size*2)
        bob.right(45)
        bob.forward(3*size)
        bob.backward(3*size)
        bob.left(90)
        bob.forward(3*size)
        bob.backward(3*size)
        bob.right(45)
    bob.backward(size*4)

def snowflake():
    size = random.randint(2,12) #randomizes snowflake size
    bob.penup()
    bob.goto(random.randint(-300,300),random.randint(-300,300)) #random pos
    bob.pendown()
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    bob.color((r,g,b)) #randomizes snowflake color
    for i in range(8): 
        branch(size)
        bob.left(45)

number = int(input("How many snowflakes would you like to generate: ")) 
for i in range(number): #asks user for number of snowflakes
    snowflake()

