import pygame as py
from pygame.locals import *

py.init()

screen = py.display.set_mode((640, 480))

player = py.image.load('./img/pnj/player.png').convert()
background = py.image.load('./img/backgrounds/fondo.png').convert()

screen.blit(background, (0, 0))

position = player.get_rect()
print(position)
screen.blit(player, position)

py.display.update()


for x in range(100):
    screen.blit(background, position, position)
    position = position.move(2, 0)
    screen.blit(player, position)
    py.display.update()
    py.time.delay(100)
