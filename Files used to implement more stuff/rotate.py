import pygame as py
game_over = False

py.init()
player =  py.image.load("enemy.png")

screen = py.display.set_mode((700,700))

player = py.transform.rotate(player,90)

while game_over is not True:
    for event in  py.event.get():

        if event.type == py.QUIT:
            game_over == True
    screen.blit(player,(350,350))
    py.display.update()