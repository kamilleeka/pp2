import pygame as pg

pg.init()
screen = pg.display.set_mode((500,500))
screen.fill((255,255,0)) #цвет фона
x = y = 400
pg.display.flip()

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit() # будет отслеживать нажатия и закрывать скрин
    keys = pg.key.get_pressed()
    if keys[pg.K_UP]:
        y -= 20
    if keys[pg.K_LEFT]:
        x -= 20
    if keys[pg.K_DOWN]:
        y += 20
    if keys[pg.K_RIGHT]:
        x += 20
    if x < 25 :
        x = 25
    if x > 500 - 25:
        x = 500 - 25
    if y < 25 :
        y = 25
    if y > 500 - 25:
        y = 500 - 25


    screen.fill((255,255,0)) # цвет фона
    pg.draw.circle(surface=screen,color=(247,10,10) , center=(x,y), radius=25)
    pg.display.flip()