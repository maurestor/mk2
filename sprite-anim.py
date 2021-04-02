
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
screen = pygame.display.set_mode((W, H))
run = 1

# shortcuts = {
#             (K_x): 'move(player_direction)',
#             (27): "pygame.quit(); sys.exit()",
#             # (K_x, 4160 + 4097 + 4352): 'print("ctl+alt+shift+X")',
#         }


def asset(dir_asset='img/player.old.png'):
    """Busca la ruta absoluta de la carpeta \'assets\' en el OS actual
    
    `Params`:
    dir_asset: str

    Sin parametros se devuelve la imagen de un personaje del juego.
    """

    path_asset = os.path.join(source_dir_file, 'assets/', dir_asset)
    return path_asset
# Carga de archivos, buscar asset()
source_dir_file = os.path.dirname(os.path.abspath(__file__))
    

font = pygame.font.SysFont('arial', 18)
# font = pygame.font.Font('./comicoro.ttf', 16)


# reloj pygame
clock = pygame.time.Clock()
t0 = time.time()

# player_loc = [0, 0]

player_move = {'left': False, 'right': False, 'up': False, 'down': False, 'last_dir':'down'}



def draw_text(text="sample", color='black', v2i=(10, 10), bg=None):
    dialogo = font.render(text, True, color, bg)
    screen.blit(dialogo, (v2i[0], v2i[1]))


def do_shortcut(event):
    """Find the the key/mod combination in the dicciotionary"""
    k = event.key
    m = event.mod

    # if (k, m) in self.shortcuts:
    if k in shortcuts:
        # exec(self.shortcuts[k, m])
        exec(shortcuts[k])



class Gamer(pygame.sprite.Sprite):
    def __init__(self, image=None, color=None, location=[0, 0], speed=3):
        pygame.sprite.Sprite.__init__(self)
        # Can you load image
        self.image = pygame.image.load(asset(image))
        self.location = location
        self.rect = Rect(self.location[0], self.location[1], 32, 64) # self.image.get_rect()
        self.speed = speed

        self.sprites = []
        self.sprites.append(self.image.subsurface(0, 0, 32, 64))    # Stay_RL0
        self.sprites.append(self.image.subsurface(32, 0, 32, 64))   # Stay_RL1
        self.sprites.append(self.image.subsurface(64, 0, 32, 64))   # Walk_RL0
        self.sprites.append(self.image.subsurface(96, 0, 32, 64))   # Walk_RL1
        
        self.sprites.append(self.image.subsurface(128, 0, 32, 64))  # Stay_up0
        self.sprites.append(self.image.subsurface(160, 0, 32, 64))  # Stay_up1
        self.sprites.append(self.image.subsurface(192, 0, 32, 64))  # Walk_up0
        self.sprites.append(self.image.subsurface(224, 0, 32, 64))  # Walk_up1
        
        self.sprites.append(self.image.subsurface(256, 0, 32, 64))  # Stay_down0
        self.sprites.append(self.image.subsurface(288, 0, 32, 64))  # Stay_down1
        self.sprites.append(self.image.subsurface(320, 0, 32, 64))  # Walk_down0
        self.sprites.append(self.image.subsurface(352, 0, 32, 64))  # Walk_down1

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect.topleft = [location[0], location[1]]
        # print(self.rect, self.rect.center)

    def update(self):
        self.current_sprite += 0.05  # reduce la velocidad del frame en tiempo
        # print(self.current_sprite)
        if self.current_sprite > len(self.sprites):
            self.current_sprite = 0

        # print(self.rect)
        if player_move['up']:
            self.location[1] -= self.speed
            player_move['last_dir'] = 'up'
        elif player_move['up'] == False:
            pass
        if player_move['down']:
            self.location[1] += self.speed
            player_move['last_dir'] = 'down'
        elif player_move['down'] == False:
            pass
        if player_move['left']:
            self.location[0] -= self.speed
            player_move['last_dir'] = 'left'
        elif player_move['left'] == False:
            pass
        if player_move['right']:
            self.location[0] += self.speed
            player_move['last_dir'] = 'right'
        elif player_move['right'] == False:
            pass

        print(player_move['last_dir'])
        # Reduccion de velocidad con int(self.current_sprite) desde la linea unicial del metodo 
        self.image = self.sprites[int(self.current_sprite)-1] 

        # if time.time() % 1 > 0.5:
        #     pygame.draw.rect(screen, RED, cursor)
        # images['gun_animation_1'] = sprite_sheet_image.subsurface(Rect(x, y, w, h))
        # images.get('gun_animation_1')

        screen.blit(self.image, self.location)
        # pygame.draw.rect(screen, 'green', (self.location[0], self.location[1], self.rect.width, self.rect.height), 1)


gamer = Gamer(image = 'img/player-anim.png')

sprite_group = pygame.sprite.Group(gamer)

plus_num = 0


def main():
    global plus_num
    run = 1
    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = 0
            elif event.type == KEYDOWN:
                # do_shortcut(event)
                if event.key == K_ESCAPE:
                    run = 0
                if event.key == K_UP:
                    player_move['up'] = True 
                if event.key == K_DOWN: 
                    player_move['down'] = True 
                if event.key == K_LEFT: 
                    player_move['left'] = True 
                if event.key == K_RIGHT: 
                    player_move['right'] = True 
            elif event.type == KEYUP:
                if event.key == K_UP: 
                    player_move['up'] = False 
                if event.key == K_DOWN: 
                    player_move['down'] = False 
                if event.key == K_LEFT: 
                    player_move['left'] = False
                if event.key == K_RIGHT: 
                    player_move['right'] = False

        screen.fill('darkgray')
        draw_text(f'Hola bienvenid@', 'black', (10, 10), 'lightgray')
        
        # dale por aqui...
        sprite_group.update()
        # sprite_group.draw(screen)

        plus_num += 1
        
        pygame.display.set_caption(f'Listo!!! {plus_num}')
        clock.tick(60)
        pygame.display.flip()
        # pygame.display.update()

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
