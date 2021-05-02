import pygame
from pygame.locals import *
from .pygamextras import screen

class Masking:
    def __init__(self, mask_size, position=False, debug=False):
        '''Generar la superficie mascara a un tamanio especifico'''
        self.mask_surf = pygame.Surface(mask_size, pygame.HWSURFACE)
        self.mask_size = mask_size
        if position:
            self.mask_rect = self.mask_surf.get_rect(position)
        else:
            self.mask_rect = self.mask_surf.get_rect()

        self.mask_surf.set_colorkey((0, 0, 0))

        self.debug = debug


    def draw(self, surface, mask_pos=[0,0], dest=[0,0], dest_offset=[0,0], area=None):
        '''Dibuja la mascara en la superficie
        
        '''
        relative_position = [-mask_pos[0], -mask_pos[1]]

        # self.mask_rect.x = mask_pos[0]; self.mask_rect.y = mask_pos[1]
        
        enmascarada = surface.copy()
        # Modify ofset?
        enmascarada.blit(self.mask_surf, (dest[0]+dest_offset[0], dest[1]+dest_offset[1]), area, pygame.BLEND_ALPHA_SDL2)
        
        self.mask_rect.x = dest[0]+dest_offset[0]
        self.mask_rect.y = dest[1]+dest_offset[1]
        self.mask_rect.w = self.mask_size[0]
        self.mask_rect.h = self.mask_size[1]
        
        surface.blit(enmascarada, (mask_pos))

        # Muestra el contorno de la mascara.
        if self.debug:
            pygame.draw.rect(screen, 'black', (dest,
                        [self.mask_rect.w, self.mask_rect.h]), 1)

        ## IMPORTANT NOTE: Recuerda establecer el rect de la mascara en el contexto donde se dibuja, no es posible aqui.
        