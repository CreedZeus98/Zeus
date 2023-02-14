from turtle import *

speed("fastest")
pencolor('black')
fillcolor('red')
fillcolor('Blue')

for i in range(3):
    fd(100)
    for i in range(3):
        begin_fill()
        fd(100)
        lt(120)
        for i in range(3):
            fd(100)
            lt(120)
        end_fill()
        lt(120)
    lt(120)

hideturtle()
mainloop()