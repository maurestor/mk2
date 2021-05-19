import pygame as pg
import pprint
from pygame.locals import *
from .pygamextras import TExtra
from random import randint
# from .bg_ui_elements import Badges


# class Items(pg.sprite.Sprite):
class Items(pg.sprite.Sprite):
    def __init__(self, image='items_lvls.png'):
        '''Lista de items de los puestos del mercadito
        mezclar con algo de est o prob...'''
        # pg.sprite.Sprite.__init__(self)
        # self.image = image
        # self.location = location

        # self.items = enumerate(self.items)

        self.list = [{"id":0, "name":"money", "quantity":500, "quality":0, "cat":0, "cost":1.00,}]
        self.newline_space = 15
        self.items_number = len(self.list)
        self.items_height = (self.newline_space * self.items_number) - self.newline_space * 2
        self.slide_y = 10
        # self.btn_plus = ()
        # self.btn_minu = ()

        self.mont = 0
        self.gen_items()


    def gen_items(self):
        pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(self.list)

        self.list = [
            # objetos de otro nivel 1
            {'id':1, 'name':'papa', 'quantity':0, 'quality':0, 'cat':1, 'cost':5.00,},
            {'id':2, 'name':'jitomate', 'quantity':0, 'quality':0, 'cat':1, 'cost':15.00,},
            {'id':3, 'name':'cebolla', 'quantity':0, 'quality':0, 'cat':1, 'cost':5.00,},
            {'id':4, 'name':'agua', 'quantity':0, 'quality':0, 'cat':1, 'cost':10.00,},
            {'id':5, 'name':'arroz', 'quantity':0, 'quality':0, 'cat':1, 'cost':23.00,},
            {'id':6, 'name':'pan', 'quantity':0, 'quality':0, 'cat':1, 'cost':2.00,},
            {'id':7, 'name':'mantequilla', 'quantity':0, 'quality':0, 'cat':1, 'cost':17.00,},
            {'id':8, 'name':'pol_pollo', 'quantity':0, 'quality':0, 'cat':1, 'cost':2.50,},
            {'id':9, 'name':'leche', 'quantity':0, 'quality':0, 'cat':1, 'cost':20.00,},
            {'id':10, 'name':'huevo', 'quantity':0, 'quality':0, 'cat':1, 'cost':30.00,},

            # objetos de otro nivel 2
            {'id':11, 'name':'pescado', 'quantity':0, 'quality':0, 'cat':'1A', 'cost':7.00,},
            {'id':12, 'name':'pollo', 'quantity':0, 'quality':0, 'cat':'1A', 'cost':7.00,},
            {'id':13, 'name':'res', 'quantity':0, 'quality':0, 'cat':'1A', 'cost':7.00,},
            {'id':14, 'name':'cerdo', 'quantity':0, 'quality':0, 'cat':'1A', 'cost':7.00,},
            {'id':15, 'name':'calamar', 'quantity':0, 'quality':0, 'cat':'1A', 'cost':7.00,},
            {'id':16, 'name':'caracol', 'quantity':0, 'quality':0, 'cat':'1A', 'cost':7.00,},
            {'id':17, 'name':'ostras', 'quantity':0, 'quality':0, 'cat':'1A', 'cost':7.00,},
            {'id':18, 'name':'camaron', 'quantity':0, 'quality':0, 'cat':'1A', 'cost':7.00,},
            {'id':19, 'name':'hueva_pez', 'quantity':0, 'quality':0, 'cat':'1A', 'cost':7.00,},

            # objetos de otro nivel 3
            {'id':20, 'name':'azucar_der', 'quantity':0, 'quality':0, 'cat':3, 'cost':7.00,},
            {'id':21, 'name':'paleta', 'quantity':0, 'quality':0, 'cat':3, 'cost':7.00,},
            {'id':22, 'name':'pas_cajeta', 'quantity':0, 'quality':0, 'cat':3, 'cost':7.00,},
            {'id':23, 'name':'pas_agri', 'quantity':0, 'quality':0, 'cat':3, 'cost':7.00,},
            {'id':24, 'name':'pas_chile', 'quantity':0, 'quality':0, 'cat':3, 'cost':7.00,},
            {'id':25, 'name':'pal_agdulce', 'quantity':0, 'quality':0, 'cat':3, 'cost':7.00,},
            {'id':26, 'name':'pal_chile', 'quantity':0, 'quality':0, 'cat':3, 'cost':7.00,},
            {'id':27, 'name':'tamarindo', 'quantity':0, 'quality':0, 'cat':3, 'cost':7.00,},
            {'id':28, 'name':'chocolate', 'quantity':0, 'quality':0, 'cat':3, 'cost':7.00,},
            {'id':29, 'name':'explo_col', 'quantity':0, 'quality':0, 'cat':3, 'cost':7.00,},
            
            # objetos de otro nivel 4
            {'id':30, 'name':'tines', 'quantity':0, 'quality':0, 'cat':4, 'cost':7.00,},
            {'id':31, 'name':'blusa', 'quantity':0, 'quality':0, 'cat':4, 'cost':7.00,},
            {'id':32, 'name':'playe_corta', 'quantity':0, 'quality':0, 'cat':4, 'cost':7.00,},
            {'id':33, 'name':'ropa_int', 'quantity':0, 'quality':0, 'cat':4, 'cost':7.00,},
            {'id':34, 'name':'short', 'quantity':0, 'quality':0, 'cat':4, 'cost':7.00,},
            {'id':35, 'name':'pantalon', 'quantity':0, 'quality':0, 'cat':4, 'cost':7.00,},
            {'id':36, 'name':'traje_baño', 'quantity':0, 'quality':0, 'cat':4, 'cost':7.00,},
            {'id':37, 'name':'falda', 'quantity':0, 'quality':0, 'cat':4, 'cost':7.00,},
            {'id':38, 'name':'falda2', 'quantity':0, 'quality':0, 'cat':4, 'cost':7.00,},
            {'id':39, 'name':'vestido', 'quantity':0, 'quality':0, 'cat':4, 'cost':7.00,},
            
            # objetos de otro nivel 5
            {'id':40, 'name':'clavos', 'quantity':0, 'quality':0, 'cat':5, 'cost':7.00,},
            {'id':41, 'name':'navaja', 'quantity':0, 'quality':0, 'cat':5, 'cost':7.00,},
            {'id':42, 'name':'tijeras', 'quantity':0, 'quality':0, 'cat':5, 'cost':7.00,},
            {'id':43, 'name':'cinta_mt', 'quantity':0, 'quality':0, 'cat':5, 'cost':7.00,},
            {'id':44, 'name':'martillo', 'quantity':0, 'quality':0, 'cat':5, 'cost':7.00,},
            {'id':45, 'name':'llave', 'quantity':0, 'quality':0, 'cat':5, 'cost':7.00,},
            {'id':46, 'name':'pinzas', 'quantity':0, 'quality':0, 'cat':5, 'cost':7.00,},
            {'id':47, 'name':'sierra', 'quantity':0, 'quality':0, 'cat':5, 'cost':7.00,},
            {'id':48, 'name':'taladro', 'quantity':0, 'quality':0, 'cat':5, 'cost':7.00,},
            {'id':49, 'name':'cortadora', 'quantity':0, 'quality':0, 'cat':5, 'cost':7.00,}
        ]
        
        for item in self.list:
            if item['cat'] == 1:
                item['quantity'] = randint(1, 10)
                item['quality'] = randint(0, 6)
            elif item['cat'] == 2:
                item['quantity'] = randint(1, 10)
                item['quality'] = randint(0, 5)
            elif item['cat'] == 3:
                item['quantity'] = randint(1, 10)
                item['quality'] = randint(0, 4)
            elif item['cat'] == 4:
                item['quantity'] = randint(1, 10)
                item['quality'] = randint(0, 3)
            elif item['cat'] == 5:
                item['quantity'] = randint(1, 10)
                item['quality'] = randint(0, 2)
        

            # if item['quantity']  == 0:
            #     print(self.list['id'], self.list['name'])


        # pp.pprint(self.list)

    def draw_items(self, mask_rect, mask_surf):
        
        for item in self.list:
            self.mont = item['cost'] * item['quantity']
            item['name'] = item['name'].replace("_", " ")
            itemx = TExtra(
                f'{item["quantity"]}, {item["name"]} ${self.mont}',
                ([mask_rect.x + 5, mask_rect.y + (item["id"] * self.newline_space + self.slide_y)]),
                'black',
                surface=mask_surf)

