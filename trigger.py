from turtle import *


def triangle_equilater(base: int, height: int = None, cor: str = "#08a4bd", fill: bool = False):
    if height == None:
        height = base

    if fill == True:
        begin_fill()

    color(cor)
    i = 0
    while i < 4:
        forward(100);
        right(90)
        i += 1
    
    if fill == True:
        end_fill()

def rect(base: int, height: int = None, cor: str = "#08a4bd", fill: bool = False):
    if height == None:
        height = base

    if fill == True:
        begin_fill()

    color(cor)
    i = 0
    while i < 4:
        forward(100);
        right(90)
        i += 1
    
    if fill == True:
        end_fill()
    

shape("turtle")
speed(1)
color("#08a4bd")

rect(100, fill = True)

done()