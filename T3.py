from turtle import *

pencolor('black')
pensize('3')
fillcolor('blue')
speed('fastest')
for i in range(10,0,-1):
    begin_fill()
    circle(i*10)
    lt(25)
    end_fill()
 
hideturtle()
mainloop()