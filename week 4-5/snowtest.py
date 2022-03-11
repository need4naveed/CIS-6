#Program that creates snowflakes with random colors and sizes
import turtle
import random

bob = turtle.Turtle()
turtle.Screen().bgcolor("grey")
colors = ['red', 'yellow', 'green', 'blue', 'purple']

def branch(size):          
    bob.forward(size*10)
    bob.right(30)
    for i in range(3):
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
    size = random.randint(4,12)
    for i in range(8):
        branch(size)
        bob.left(45)
    
        

snowflake()

#    for i in range(3):        
#        for i in range(3):
#            bob.forward(3 * size)
#            bob.backward(3 * size)
#            bob.right(45)
#        bob.left(90)
#        bob.backward(3 * size)
#        bob.left(45)
#    bob.right(90)
#    bob.forward(9 * size)
