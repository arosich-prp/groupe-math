# -*- coding: utf-8 -*-

#import de la bibliothèque turtle.
from turtle import *

#La procédure permetant de tracer le triangle.
def triangle(cote) :
    pendown()
    for i in range(3):
        forward(cote)
        left(120)
    penup()


# le programme principal tel que proposé lors de la session DNB.
clear()
penup()
goto(-200,-100)
setheading(0)
cote=100
for i in range(5):
    triangle(cote)
    forward(cote)
    cote=cote-20
exitonclick() # permet une sortie propre du graphique.


