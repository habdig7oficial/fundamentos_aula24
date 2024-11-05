from turtle import *

class Shapes(Turtle):
    def __init__(self, new_shape: str = "turtle", new_speed: int = 5, new_color: str = "#08a4bd", fill: bool = False):
        self.new_color = new_color
        self.fill = fill
        self.new_shape = new_shape
        self.new_speed = new_speed
        shape(self.new_shape)
        speed(self.new_speed)
        color(self.new_color)

    ## Exercicio 1
    def rect(self, base: int, height: int = None):
        if height == None:
            height = base

        if self.fill == True:
            begin_fill()

        color(self.new_color)
        i = 0
        while i < 4:
            forward(base if i % 2 == 0 else height);
            right(90)
            i += 1
        
        if self.fill == True:
            end_fill()
    ## Exercicio 2
    def eq_triangle(self, sides: int):
        if self.fill == True:
            begin_fill()
        i = 0
        while i < 3:
            forward(sides)
            left(60 * 2)
            i += 1
        
        if self.fill == True:
            end_fill()
    
    ## Exercicio 3
    def paralelogram(self, base: int, height: int = None, degrees: int = 90):
        if height == None:
            height = base

        if self.fill == True:
            begin_fill()

        color(self.new_color)
        i = 0
        while i < 4:
            forward(base if i % 2 == 0 else height);
            if degrees != 90:
                right(degrees * 2 if i % 2 == 0 else degrees)
            else:
                right(degrees)
            i += 1
        
        if self.fill == True:
            end_fill()

    def go_to(self, line_x: int = 0, line_y: int = 0):
        penup()
        forward(line_x)
        left(90)
        forward(line_y)
        right(90)
        pendown()

        


