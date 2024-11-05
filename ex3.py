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

div = 2

canvas.go_to(line_x= -((basic / div) + ((basic / (div * 2)) / div)), line_y = -(basic / div))
canvas.rect(basic / (div * 2), basic / div)
canvas.go_to(line_x= (basic + div), line_y = (basic / (div * 2)))
canvas.rect(basic / div, basic / (div * 2))
canvas.go_to(line_x = (basic / div) + (basic / (div * 1.5)))
canvas.rect(basic / div, basic / (div * 2))

canvas.go_to(line_x = (basic / div) + (basic / (div * 1.5)) + 10)
done()