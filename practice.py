from turtle import *

speed('slowest')
pencolor('black')
fillcolor('yellow')

for i in range(3):
    fd(100)
    for i in range(3):
        begin_fill()
        fd(100)
        left(120)
        fd(100)
        left(120)
        fd(100)
        left(120)
        for i in range(3):
            fd(100)
            left(120)
            fd(100)
            left(120)
            fd(100)
            left(120)
end_fill()

hideturtle()
mainloop()