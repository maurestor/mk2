import pygame
from pygame.locals import *


class Events:
    
    def get_event(self, event):
        # Es mas recomendable utilizar
        # pygame.event.pump()
        # print(self.mask_rect)
    
        ''' Mecanismo de movimiento con el scroll/rueda del raton
        '''
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4 and self.mask_rect.collidepoint(event.pos):
                if self.slide_y > -self.items_height:
                    self.slide_y -= 10
                # print('arriba')
            elif event.button == 5 and self.mask_rect.collidepoint(event.pos):
                if self.slide_y < 10:
                    self.slide_y += 10
                # print('abajo')

        # print(self.slide_y)

        
    

        
