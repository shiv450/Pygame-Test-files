import pygame as py
from pygame import mixer as mx
import random as r
import copy as c
py.init()

#game_over is the variable that controlls if the game window is running
game_over = False

#screen is the variable of the display
screen = py.display.set_mode((700,700))

#the variable that controlls the name of the window
caption = py.display.set_caption("Space invaders")



#loading in the music
mx.init()
mx.music.load(r"background.wav")
mx.music.set_volume(0.5)
mx.music.play()

#loading in the background image, icon image and setting them to be the same
Bg = py.image.load("background.png")
Bg = py.transform.scale(Bg,(700,700))

icon_image = py.image.load("ufo.png")
icon = py.display.set_icon(icon_image)

#these are the coords of the player on the x axis and y axis
coordsx = 325
coordsy = 600

# ecoordsx = r.randint(1,700)
# ecoordsy = r.randint(1,100)

#these are the starting coords of the enemy
ecoordsx = 100
ecoordsy = 0

#loading in the images for the bullet, enemy and player
ammo = py.image.load(r"bullet.png")
enem = py.image.load(r"enemy.png")
rocket =  py.image.load(r"player.png")

#making functions to put them on the screen
def player(image,x,y):
    screen.blit(image,(x,y))
playerxchange = 0

def bullet(image,x,y):
    screen.blit(image,(x,y))
bulletychange = 0
bullet_state = 0
n_coordsy = 625

def enemy(image,x,y):
    screen.blit(image,(x,y))
enemyxchange = 5
enemyychange = 0

#the game loop, this makes the game run
while game_over is not True:
    screen.blit(Bg,(0,0))
    
    #getting the events
    for event in py.event.get():
    
        #if the event is quit (if the red cross is pressed), game_over = true
        if event.type == py.QUIT:
            game_over = True
    
        #checking for the keys pressed
        if event.type == py.KEYDOWN:
    
            #if the key pressed is the left arrow, the player coordsx -= 1 and if the right key is pressed, players coordsx is += 1
            if event.key == py.K_LEFT:
                playerxchange = -1
            if event.key == py.K_RIGHT:
                playerxchange = 1
    
            #if the event is space, n_coordsx = coordsx
            if event.key == py.K_SPACE:
                bullet_state = 1
                if bullet_state == 1:
                    n_coordsx = coordsx
    
        #checking events for when the key goes up
        elif event.type == py.KEYUP:
            if (event.key == py.K_LEFT) or (event.key == py.K_RIGHT):
                playerxchange = 0
    
    #making coordsx += or -= 1 depeding on what key was pressed
    coordsx = coordsx+playerxchange
    
    #making sure the player can't leave the game window
    if coordsx < 50:
        coordsx = 50
    if coordsx > 650:
        coordsx = 650
    
    #putting the player on the screen
    player(rocket,coordsx,coordsy)
    
    #enemy logic
    ecoordsx = ecoordsx + enemyxchange
    if ecoordsx < 0:
        enemyxchange = 5
        ecoordsy = ecoordsy + 50
    if ecoordsx > 625:
        enemyxchange = -5
        ecoordsy = ecoordsy + 50
    
    if bullet_state == 1:
        #n_coordsy = coordsy
        bullet(ammo,n_coordsx+36.5,n_coordsy+10)
        bullet(ammo,n_coordsx-5,n_coordsy+10)
        n_coordsy -= 10
        if n_coordsy <= 0:
            bullet_state = 0
            # n_coordsy = coordsx
            n_coordsy = coordsy

    #putting the enemy and bullets on the screen
    enemy(enem,ecoordsx,ecoordsy)
    bullet(ammo,coordsx-5,coordsy+5)
    bullet(ammo,coordsx+36.5,coordsy+5)
    
    #updating display
    py.display.update()