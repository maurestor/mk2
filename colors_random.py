import pygame, random
from pygame.locals import *
import sys
import time



pygame.init()
W, H = 600, 400
screen = pygame.display.set_mode((W, H))
font = pygame.font.SysFont('comicoro', 200)

# reloj pygame
clock = pygame.time.Clock()
t0 = time.time()

class TextColors:
    def __init__(self):
        self.counter = 0
        self.color0 = self.color1 = self.color2 = (255)

    def colorize(self):
        '''Return color random range'''
        self.counter += 1
        if self.counter >= 5:
            self.counter = 0
            self.color0 = random.randrange(50, 255)
            self.color1 = random.randrange(50, 255)
            self.color2 = random.randrange(50, 255)
        return (self.color0, self.color1, self.color2)


    def update(self):
        '''Update color &of text every "n" frames per second(1000fps)'''
        self.counter += 1
        if self.counter >= 10: #every frame in 1000
            self.counter = 0
            self.color0 = random.randrange(100, 255)
            self.color1 = random.randrange(100, 255)
            self.color2 = random.randrange(100, 255)
        
        # texto = font.render(f'Color {self.counter:.0f}', True, (self.color0, self.color1, self.color2))
        texto = font.render(f'Color', True, (self.color0, self.color1, self.color2))
        screen.blit(texto, [W//2-120, H//2-100])
        

def main():
    # counter = 0
    textcolor= TextColors()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()

        screen.fill('gray10')

        textcolor.update()
        
        clock.tick(60)
        pygame.display.flip()
        # pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()