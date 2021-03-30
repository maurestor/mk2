#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pygame
import os
import sys
import time
from pygame.locals import *
from src.poswin import PosWin


pygame.init()
pos = PosWin()
W, H = 600, 400
pos.pos_rand(W, H)
screen = pygame.display.set_mode((W, H))

# font = pygame.font.SysFont('arial', 18)
font = pygame.font.Font(os.path.join('./assets/fonts/comicoro.ttf'), 16)

# reloj pygame
clock = pygame.time.Clock()
t0 = time.time()


def draw_text(text="sample", color='black', v2i=(10, 10), bg=None):
    dialogo = font.render(text, True, color, bg)
    screen.blit(dialogo, (v2i[0], v2i[1]))


class Gamer(pygame.sprite.Sprite):
    def __init__(self, image=None, color=None, v2i=(None, None)):
        pygame.sprite.Sprite.__init__(self)

        # Can you load image
        if image != None:
            self.image = pygame.image.load(image)
            self.rect = self.image.get_rect()
            print(self.rect, self.rect.center)
        else:
            self.image = pygame.Surface([v2i[0], v2i[1]])
            if color == None:
                color = 'green'
            else:
                self.image.fill(color)

    def draw(self):
        screen.blit(self.image, (100, 100))
        pygame.draw.rect(screen, 'green', (100, 100, self.rect.width, self.rect.height), 1)

class Collider(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pass

    def draw(self):
        pygame.draw.rect(screen, 'green', (200, 200, 100, 100), 1)


gamer = Gamer(image = './assets/img/player.old.png')
collider = Collider()

def main():
    run = 1
    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = 0
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = 0

        screen.fill('darkgray')
        draw_text("Hola, cambiame...", 'black', (10, 10), 'lightgray')
        # dale por aqui...
        gamer.draw()
        collider.draw()

        clock.tick(60)
        pygame.display.flip()
        # pygame.display.update()

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
