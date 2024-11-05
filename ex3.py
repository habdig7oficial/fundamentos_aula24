from trigger import *


basic = 100

canvas = Shapes(new_color = "#C0504D", fill = True, new_speed = 1)
canvas.eq_triangle(basic)
canvas.new_color = "#FF8200"
canvas.rect(basic)
canvas.go_to(basic)
canvas.new_color = "#FFC000"
canvas.rect(basic * 2, basic)
canvas.new_color = "#C00000"
canvas.paralelogram(basic * 2, basic, degrees = -60)
canvas.new_color = "#000000"
#canvas.paralelogram(200)
done()