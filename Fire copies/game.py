import pygame as py
from pygame import mixer as mx
import random as r

py.init()

game_over = False

screen = py.display.set_mode((700,700))

caption = py.display.set_caption("Space invaders")

mx.init()
mx.music.load(r"background.wav")
mx.music.set_volume(0.5)
mx.music.play()

Bg = py.image.load("background.png")

Bg = py.transform.scale(Bg,(700,700))

icon_image = py.image.load("ufo.png")

icon = py.display.set_icon(icon_image)

coordsx = 325
coordsy = 600

# ecoordsx = r.randint(1,700)
# ecoordsy = r.randint(1,100)

ecoordsx = 100
ecoordsy = 0

enem = py.image.load(r"enemy.png")
rocket =  py.image.load(r"player.png")

def player(image,x,y):
    screen.blit(image,(x,y))
playerxchange = 0


def enemy(image,x,y):
    screen.blit(image,(x,y))
enemyxchange = 0
enemyychange = 0

while game_over is not True:
    screen.blit(Bg,(0,0))
    for event in py.event.get():
        if event.type == py.QUIT:
            game_over = True
        if event.type == py.KEYDOWN:
            if event.key == py.K_LEFT:
                playerxchange = -1
            if event.key == py.K_RIGHT:
                playerxchange = 1
        elif event.type == py.KEYUP:
            if (event.key == py.K_LEFT) or (event.key == py.K_RIGHT):
                playerxchange = 0
    coordsx = coordsx+playerxchange
    if coordsx < 50:
        coordsx = 50
    if coordsx > 650:
        coordsx = 650
    player(rocket,coordsx,coordsy)
    if ecoordsx < 50:
        ecoordsx = 50
        enemyxchange = 1
        ecoordsy = ecoordsy + 5
    elif ecoordsx > 650:
        ecoordsx = 650
        ecoordsy = ecoordsy + 5
        enemyxchange = -1
    if ecoordsx > 0:
        ecoordsx = ecoordsx + enemyxchange
    if ecoordsx < 700:
        ecoordsx = ecoordsx + enemyxchange
    enemy(enem,ecoordsx,ecoordsy)
    py.display.update()