from turtle import * # import turtle module

speed('fastest')

side = 10
size = 100

# create a hexagon
for i in range(side):
    fd(size)
    lt(360/side)
    write(i)
hideturtle()            # hide turtle
mainloop()              # keep window open