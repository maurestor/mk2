#!/usr/bin/env python
#-*- coding:utf-8 -*-

try:
    import pygame
    from pygame.locals import *
    import sys
    import time
    import random
    from src.poswin import PosWin
except ImportError as IErr:
    print(f'Se importaron mal esta/s librerias, {IErr}.')


def draw_text(text, color, x, y, bg=None):
    dialogo = font.render(text, True, color, bg)
    screen.blit(dialogo, (x, y))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./assets/img/player.png')

    def update(self):
        pos = pygame.mouse.get_pos()


pygame.init()
# pos = PosWin()
W, H = 600, 400
center_W, center_H = W//2, H//2


screen = pygame.display.set_mode((W, H))
font = pygame.font.SysFont('arial', 18)


# reloj pygame
clock = pygame.time.Clock()
t0 = time.time()

play = Player()

player_img = pygame.image.load('./assets/img/player.png')
# Posicion del personaje
player_w = 32
player_h = 64
player_img = player_img
player = player_img.subsurface(0, 0, player_w, player_h) # recorte del sprite del punto Axy al Bxy
player = pygame.transform.rotate(screen, 18)
# player = pygame.transform.scale(player, (int(player_w*1.5), int(player_h*1.5)))
player = player.convert_alpha()


# cubo_size = player_sprite.get_rect()

cubo_x = 32
cubo_y = 64
# cubo_x = player.get_width()
# cubo_y = player.get_height()
incr = [0, True]
rect = Rect(W//2, H//2, cubo_x, cubo_y)
print(f'x={rect.x}, y={rect.y}, w={rect.w}, h={rect.h}')
print(f'left={rect.left}, top={rect.top}, right={rect.right}, bottom={rect.bottom}')
print(f'center={rect.center}')

def main():
    global player
    runnig = True
    while runnig:
        screen.fill('darkblue')
        for event in pygame.event.get():
            if event.type == QUIT:
                runnig = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    runnig = False

  
        pygame.draw.line(screen, 'darkgray', (0, H//2), (W, H//2), 1)
        pygame.draw.line(screen, 'darkgray', (W//2, 0), (W//2, H), 1)
        pygame.draw.rect(screen, 'gold', rect, 1)
        screen.blit(player, (W//2, H//2)) # posicion del jugador

        clock.tick()
        pygame.display.flip()
    
    
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()