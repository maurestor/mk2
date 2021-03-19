import pygame as pg
import sys
from pygame.locals import *

class GameObject:
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height) 
    def move(self):
        self.pos = self.pos.move(0, self.speed)
        if self.pos.right > 600:
            self.pos.left = 0

pg.init()

screen = pg.display.set_mode((800, 600))

player = pg.image.load('./img/pnj/player.png')
background = pg.image.load('./img/backgrounds/fondo.png').convert()
screen.blit(background, (0, 0))

# position = player.get_rect()
# print(position)
# screen.blit(player, position)
# pg.display.update()
# for x in range(100):
#     screen.blit(background, position, position)
#     position = position.move(2, 0)
#     screen.blit(player, position)
#     pg.display.update()
#     pg.time.delay(100)
objects = []
for x in range(10):
    o = GameObject(player, x * 40, x)
    objects.append(o)

running = True
while running:
    for e in pg.event.get():
        if e.type in (QUIT, KEYDOWN):
            pg.quit()
            sys.exit()
    for o in objects:
        screen.blit(background, o.pos, o.pos)
    for o in objects:
        o.move()
        screen.blit(o.image, o.pos)

    pg.display.update()
    pg.time.delay(100)
