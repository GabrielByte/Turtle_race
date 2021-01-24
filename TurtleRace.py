# Let's make a turtle race

from turtle import *
from random import randint

speed(10)
penup()
goto(-140, 140)

for step in range(16):
    write(step, align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

ada = Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.right(360)
ada.goto(-160, 100)
ada.pendown()

bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.right(360)
bob.goto(-160, 70)
bob.pendown()

jim = Turtle()
jim.color('green')
jim.shape('turtle')

jim.penup()
jim.right(360)
jim.goto(-160, 40)
jim.pendown()

sam = Turtle()
sam.color('yellow')
sam.shape('turtle')

sam.penup()
sam.right(360)
sam.goto(-160, 10)
sam.pendown()

for turn in range(100):
    ada.forward(randint(1,5))
    bob.forward(randint(1,5))
    jim.forward(randint(1,5))
    sam.forward(randint(1,5))