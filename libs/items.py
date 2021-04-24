import pygame
from pygame.locals import *
# from .pygamextras import asset, H, W
from random import randint


class Items(pygame.sprite.Sprite):
    def __init__(self, image='items_lvls.png', location=[0,0]):
        '''Lista de items de los puestos del mercadito
        mezclar con algo de est o prob...'''
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.location = location

    def listing(self):
        items_lvls = [
            # objetos de otro nivel 1
            "papa", "jitomate", "cebolla", "agua", "arroz", "pan", "mantequilla", "polvo de pollo", "leche", "huevo",
            # objetos de otro nivel 2
            "pescado", "pollo", "res", "cerdo", "calamar", "caracol", "ostras", "camaron", "caviar", 
            # objetos de otro nivel 3
            "azucar derretida", "paleta", "pastilla cajeta", "pastilla agridulce", "pastilla con chile", "paleta agridulce", "paleta centro chile", "tamarindo", "chocolate", "explosion de colores", 
            # objetos de otro nivel 4
            "tines", "blusa", "playe corta", "ropa interior", "short", "pantalon", "traje de baño", "falda", "falda2", "vestido", 
            # objetos de otro nivel 5
            "clavos", "navaja", "tijeras", "cinta metrica", "martillo", "llave", "pinzas", "sierra", "taladro", "cortadora"
        ]
        for l in items_lvls:
            print(l)


    def items(self):
        lvls = {
            # objetos de otro nivel 1
            "papa", "jitomate", "cebolla", "agua", "arroz", "pan", "mantequilla", "polvo de pollo", "leche", "huevo",
            # objetos de otro nivel 2
            "pescado", "pollo", "res", "cerdo", "calamar", "caracol", "ostras", "camaron", "caviar", 
            # objetos de otro nivel 3
            "azucar derretida", "paleta", "pastilla cajeta", "pastilla agridulce", "pastilla con chile", "paleta agridulce", "paleta centro chile", "tamarindo", "chocolate", "explosion de colores", 
            # objetos de otro nivel 4
            "tines", "blusa", "playe corta", "ropa interior", "short", "pantalon", "traje de baño", "falda", "falda2", "vestido", 
            # objetos de otro nivel 5
            "clavos", "navaja", "tijeras", "cinta metrica", "martillo", "llave", "pinzas", "sierra", "taladro", "cortadora"
        }
lista = Items()
lista.listing()