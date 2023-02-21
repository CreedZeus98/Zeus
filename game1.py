import pgzrun

# add bgm Music
music.play('bgm')

b = Rect((100,100), (100,50))
b = Actor('img1', (300,300))
vx,vy = 5, 1 # global variable                   # vx= velocity on x-axis

def draw():
    screen.fill('Red')
    b.draw()

def update():
    global vx,vy
    b.x += vx
    b.y += vy
    if b.right > 800 or b.left < 0:
        vx = -vx
        sounds.s1.play()
    if b.bottom > 600 or b.top < 0:
        vy = -vy
        sounds.s1.play()
# outside of all function
pgzrun.go()