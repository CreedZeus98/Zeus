from turtle import *

speed('fast')
pencolor('Blue')

gap = 5
angle = 60
for i in range (100):
    fd(i*gap)
    lt(angle)
    write(i)
    
hideturtle()
mainloop()