import pygame as pg
import os
from pygame.locals import *
from pygame.mask import Mask
from libs.items import Items
from libs.pygamextras import Masking

pg.init()
W, H = 1280//2, 960//2
os.environ['SDL_VIDEO_WINDOW_POS'] = f"{50},{50}"

SCREEN = pg.display.set_mode((W, H), flags=RESIZABLE|SRCALPHA|DOUBLEBUF|HWACCEL|NOFRAME)

clock = pg.time.Clock()


items = Items()
menu = Masking((300, 150), debug=1)

def main():
    running = True
    while running:
        SCREEN.fill('gray50')
        mouse_pos = pg.mouse.get_pos()

        for event in pg.event.get():
            if event.type == QUIT:
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()

        pg.draw.rect(SCREEN, 'green', [mouse_pos[0], mouse_pos[1], 15, 15], 0)
        


        items_rect = Rect(0,0,200,100)
        items.draw_items(items_rect, menu.mask_surf)

        menu.draw(SCREEN, (0,0))


        clock.tick(60)
        # pg.display.flip()
        pg.display.update()
    pg.quit()
    sys.exit()

if __name__ == '__main__':
    main()