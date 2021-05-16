import pygame
from pygame.locals import *
from .pygamextras import *
from .items import Items

class Stores(pygame.sprite.Sprite, Masking):

    def __init__(self, location=[0,0], pid=1, multi=False):
        pygame.sprite.Sprite.__init__(self)

        self.items = Items()
        
        Masking.__init__(self, [0,0])

        self.slide_y = 0

        self.image = pygame.image.load(asset('assets/img','stores-anim.png'))
        self.rect = self.image.get_rect(top=128)
        self.rect.w = 128
        # self.source_rect
        # self.rect.y = 128
        self.rect.x = location[0]
        self.rect.y = location[1]
        
        # self.collide_rect = Rect(self.rect.left, self.rect.top + 128, self.rect.w, self.rect.h-96)
        
        self.pid = pid
        self.location = location

        self.sprites = []
        self.sprites.append(self.image.subsurface(0, 0, 128, 128))    # Stay_R0
        self.sprites.append(self.image.subsurface(128, 0, 128, 128))   # Stay_R1
        self.current_sprite = 0
        self.frame = 0

        self.spritesheet = self.sprites
        
        self.vars = {'id':pid, 'type':'basic', 'location':[location[0], location[1]]}
        
        #moving plus and minus
        self.moving = [0, True]
        self.action = ActionBadges()
        self.textcolor = TextColors()
        self.items = Items()

        self.counter = 0

        # self.newpos = []



    def dialogue_box(self):
        #Bounce list
        
        # Render mask ##########################
        mask = Masking((250, 100), debug=1)

        # self.cube.rotate('gold', [50,50, 100,100], mask.mask_surf)
        pygame.draw.rect(mask.mask_surf, 'gray75', (0,0,250, 100), 0)
        

        newline_space = 15
        items_number = len(self.items.item_list)
        self.items_height = (newline_space*items_number)-newline_space*2
        
        btn_plus = ()
        btn_minus = ()
        item_var = []
        # Renderizado desde Items
        for item in self.items.item_list:
            item['name'] = item['name'].replace("_", " ")

            mont = item['cost'] * item['quantity']
            itemx = TExtra(
                f'{item["quantity"]}, {item["name"]} ${mont}',
                ([mask.mask_rect.x + 5,
                mask.mask_rect.y + (item["id"] * newline_space + self.slide_y)]),
                'black', surface=mask.mask_surf)
            


        tit_dialog = TExtra('Tienda X - Items', [5,0], bgcolor='gray50', surface=mask.mask_surf)
        #texto de ejemplo para poner texto
        # textra('Hola!!!', [mask.mask_rect.x+5, mask.mask_rect.y+15+self.slide_y], surface=mask.mask_surf)
        
        
        mask.draw(screen, (0,0), (self.rect.right, self.rect.top-50))

        # Se debe establecer la posicion de mask_rect en el contexto/ambito 
        self.mask_rect.x = self.rect[0]+128;self.mask_rect.y = self.rect[1]-50
        self.mask_rect.w = 250;self.mask_rect.h = 100
        # self.mask_rect = self.rect
        pygame.draw.rect(screen, 'black', (self.mask_rect), 1)
        # print(self.rect, self.mask_rect)
        
        # Render mask ##########################
        
        # self.cube.rotate('blueviolet', [100,100,200,200], screen)
    

    def interaction(self):

        if key_press['F4_key']:
            pygame.draw.rect(screen, 'gold', (self.rect.x, self.rect.y, self.rect.w, self.rect.h), 1, 5)

            pos_store = TExtra(f'pos: {self.rect.x}, {self.rect.y}', [self.rect.x, self.rect.y-20], 'darkslategray1')
            
        self.dialogue_box()

            #Salto en debug
            # self.slide_y = bounce(self.items.items_height, 0, 1)
        
        pygame.draw.rect(screen, 'red', [
                self.rect.x,
                self.rect.y,
                self.rect.w,
                self.rect.h],
                1, 5)

        # Llamar a los dialogos


    def get_event(self, event):
        # Es mas recomendable utilizar
        # pygame.event.pump()
        # print(self.mask_rect)
    
        ''' Mecanismo de movimiento con el scroll/rueda del raton
        '''
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4 and self.mask_rect.collidepoint(event.pos):
                if self.slide_y > -self.items.items_height:
                    self.slide_y -= 10
                # print('arriba')
            elif event.button == 5 and self.mask_rect.collidepoint(event.pos):
                if self.slide_y < 10:
                    self.slide_y += 10
                # print('abajo')


    def control(self, x, y):
        """
        control player movement
        """
        self.rect.x += x
        self.rect.y += y
    

    def update(self, pos=[0, 0]):
        
        self.current_sprite += 0.05  # aumente # de frames entre cada FPS
        if self.current_sprite > len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)-1] # si es entero cambiar frame

        # self.movement(pos)

        self.vars['location'][0] = self.rect.x
        self.vars['location'][1] = self.rect.y



class StoreBg(pygame.sprite.Sprite):
    '''Usar esta clase para colisionar '''
    def __init__(self, location=[0,0], pid=1, multi=False):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(asset('assets/img', 'floor.png'))
        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]+108
        self.counter = 0
    
    def control(self, x, y):
        """
        control player movement
        """
        self.rect.x += x
        self.rect.y += y

    def interaction(self):
        #Establecer rect despues de su asignacion NO MOVER!!!
        # self.collide_rect = self.rect
        # x = self.collide_rect.x
        # y = self.collide_rect.y+128
        # self.collide_rect.height = 32

        pos_store_bg = TExtra(f'pos: {self.rect.x}, {self.rect.y}', [self.rect.x, self.rect.y-20], 'deepskyblue')
        
        pygame.draw.rect(screen, 'red', [
                self.rect.x,
                self.rect.y,
                self.rect.w,
                self.rect.h],
                1, 5)
        
        # screen.blit(self.surface, [self.rect.x, self.rect.y+128])
    def update(self):
        pass
        # self.counter += 0.01
        # self.rect.move_ip(self.counter, 0)