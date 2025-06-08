import pygame
# from pygame import color # Unused
# from pygame import surface # Unused
from pygame.locals import *
from .pygamextras import *
from .items import Items

# Store type constants
STORE_TYPE_DEFAULT = None # Or a specific string like 'default_store'
STORE_TYPE_GREEN = 'green'
STORE_TYPE_DARK_GREEN = 'dark_green'


class Stores(pygame.sprite.Sprite, Masking):

    def __init__(self, stores_anim_sheet_surface, location=[0,0], storetype=STORE_TYPE_DEFAULT, store_id=0): # Added stores_anim_sheet_surface, use constant
        pygame.sprite.Sprite.__init__(self)

        self.items = Items()
        
        Masking.__init__(self, [0,0])

        self.slide_y = 0
        self.sprites = []

        # self.image = pygame.image.load(asset('assets/img','stores-anim.png')) # Removed direct loading
        self.image_sheet = stores_anim_sheet_surface # Use the passed surface

        if storetype == STORE_TYPE_GREEN:
            self.sprites.append(self.image_sheet.subsurface(0, 128, 128, 128))
        elif storetype == STORE_TYPE_DARK_GREEN:
            self.sprites.append(self.image_sheet.subsurface(0, 256, 128, 128))
        else: # Default store type
            self.sprites.append(self.image_sheet.subsurface(0, 0, 128, 128))
            self.sprites.append(self.image_sheet.subsurface(128, 0, 128, 128))
        
        
        # self.sprites.append(self.image_sheet.subsurface(0, 0, 128, 128))    # Stay_R0
        # self.sprites.append(self.image_sheet.subsurface(128, 0, 128, 128))   # Stay_R1

        # The self.image will be set in the update() method or after sprite selection
        if self.sprites:
            self.image = self.sprites[0] # Initialize self.image with the first sprite
            self.rect = self.image.get_rect()
        else:
            # Fallback if no sprites were loaded (should not happen with correct storetype)
            self.image = pygame.Surface((128,128)) # Placeholder
            self.image.fill((255,0,255)) # Magenta to indicate error
            self.rect = self.image.get_rect()

        # self.rect = self.image.get_rect(top=128) # Old way, rect is now derived from the actual sprite
        self.rect.w = 128
        self.rect.h = 128
        # self.source_rect
        self.rect.x = location[0]
        self.rect.y = location[1]
        
        # self.collide_rect = Rect(self.rect.left, self.rect.top + 128, self.rect.w, self.rect.h-96)
        
        self.store_id = store_id
        self.location = location

        self.current_sprite = 0
        self.frame = 0

        self.spritesheet = self.sprites
        
        
        #moving plus and minus
        self.moving = [0, True]
        self.action = ActionBadges()
        self.textcolor = TextColors()
        self.items = Items()

        self.counter = 0
        self.prld = 0
        self.prld_x = 0
        self.prld_y = 0
        self.rect_btn_plus = [0,0]
        self.rect_btn_minu = [0,0]
        self.txt_rect = Rect(0,0,0,0)
        # self.newpos = []
        # self.colors= TextColors()
        self.rectn = self.rect
        self.slide_y = 10

        self.vars = {'id':store_id, 'type':'basic', 'location':[location[0], location[1]], 'total_store':0, 'total_items':0}
        
        total = 0
        items = 0

        for item in self.items.list:
            mont = item['cost'] * item['quantity']
            total += mont
            items += item['quantity']

        self.vars['total_store'] = total
        self.vars['total_items'] = items
        
        self.color = TextColors()


    def get_event(self, event):
        # Es mas recomendable utilizar
        # pygame.event.pump()
        # print(self.mask_rect)
    
        ''' Mecanismo de movimiento con el scroll/rueda del raton
        '''
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 5 and self.mask_rect.collidepoint(event.pos):
                if self.slide_y > -self.items.items_height:
                    self.slide_y -= 10
                # print('arriba')
            elif event.button == 4 and self.mask_rect.collidepoint(event.pos):
                if self.slide_y < 10:
                    self.slide_y += 10
                # print('abajo')
            # for item in self.items.list:
            #     boton_mas = DialogueButtons(self.mask_surf, self.rect_btn_plus)
            #     print(boton_mas.rect)
            #     if event.button == 1 and pygame.Rect.collidepoint(boton_mas.rect, event.pos):
            #         item['quantity'] += 1
            #         print(f'{item["name"]} (+)')



    def interaction(self, *arg):
        for var in arg:
            pass
        if key_press['F4_key']:
            pygame.draw.rect(screen, 'gold', (self.rect.x, self.rect.y, self.rect.w, self.rect.h), 1, 5)

            pos_store = TExtra(f'pos: {self.rect.x}, {self.rect.y}', [self.rect.x, self.rect.y-20], 'darkslategray1')
            

            # Salto en debug
            self.slide_y = bounce(self.items.items_height, 0, 1)
        
        # pygame.draw.rect(screen, 'red', [
        #         self.rect.x,
        #         self.rect.y,
        #         self.rect.w,
        #         self.rect.h],
        #         1, 5)

        # self.dialogue_box()

        # Llamar a los dialogos



    def dialogue_box(self):
        #Bounce list
        
        # Render mask ##########################
        
        mask = Masking((250, 150), debug=1) # This uses Masking from pygamextras

        newline_space = 15
        items_number = len(self.items.list)
        self.items_height = (newline_space*items_number)-newline_space*2

        # self.cube.rotate('gold', [50,50, 100,100], mask.mask_surf)
        mask.mask_surf.set_alpha(230)
        pygame.draw.rect(mask.mask_surf, 'gray65', (0,0,250, 150), 0)

        total = 0
        items = 0
        # Renderizado desde Items
        for item in self.items.list:
            # colorized1 = self.colors.colorize(50, 255)
            # colorized2 = self.colors.colorize(0, 200)

            pygame.draw.rect(mask.mask_surf, 'green', (self.prld_x-39, self.prld_y, 12,12), 0, 3)
            pygame.draw.rect(mask.mask_surf, 'chocolate1', (self.prld_x-24, self.prld_y, 12,12), 0, 3)
            pygame.draw.rect(mask.mask_surf, 'green4', (self.prld_x-39, self.prld_y, 12,12), 2, 3)
            pygame.draw.rect(mask.mask_surf, 'chocolate3', (self.prld_x-24, self.prld_y, 12,12), 2, 3)
            # print(self.rect_btn_plus)
            item['name'] = item['name'].replace("_", " ")

            mont = item['cost'] * item['quantity']
            
            # pos-rect_list_dialogues
            self.prld_x = mask.mask_rect.x + 45
            self.prld_y = mask.mask_rect.y + (item["id"] * newline_space + self.slide_y)
            self.prld = (self.prld_x, self.prld_y)
            
            itemx = TExtra(
                f'{item["quantity"]}, {item["name"]} ${mont}', self.prld, 'gray1', surface=mask.mask_surf)
            
            self.txt_rect = itemx.texto_rect
            self.rect_btn_plus = (self.prld_x+self.rect.x+90, self.prld_y+self.rect.y-51)
            self.rect_btn_minu = (self.prld_x+self.rect.x+105, self.prld_y+self.rect.y-51)

            
            # print(txt_rect)
            boton_mas = DialogueButtons(mask.mask_surf, self.rect_btn_plus)
            if pygame.Rect.collidepoint(boton_mas.rect, mouse.get_pos()):
                item['quantity'] += 1
                # print(f'{item["name"]} (+)')

            boton_menos = DialogueButtons(mask.mask_surf, self.rect_btn_minu)
            if pygame.Rect.collidepoint(boton_menos.rect, mouse.get_pos()):
                if item['quantity'] > 0:
                    item['quantity'] -= 1
                # print(f'{item["name"]} (-)')


            total += mont
            items += item['quantity']

            # print(mont)

        self.vars['total_store'] = total
        self.vars['total_items'] = items
        

        tit_dialog = TExtra(f'Tienda X - Items ({self.vars["total_items"]}) Tot:${self.vars["total_store"]}', [5,0], 'gray1', bgcolor='gray50', surface=mask.mask_surf)
        #texto de ejemplo para poner texto
        # textra('Hola!!!', [mask.mask_rect.x+5, mask.mask_rect.y+15+self.slide_y], surface=mask.mask_surf)
        
        
        mask.draw(screen, (0,0), (self.rect.right, self.rect.top-50))

        # Se debe establecer la posicion de mask_rect en el contexto/ambito 
        self.mask_rect.x = self.rect[0]+128;self.mask_rect.y = self.rect[1]-50
        self.mask_rect.w = 250;self.mask_rect.h = 150
        # self.mask_rect = self.rect
        pygame.draw.rect(screen, 'black', (self.mask_rect), 1)
        # print(self.rect, self.mask_rect)

        # Render mask ##########################

        # self.cube.rotate('blueviolet', [100,100,200,200], screen)


    
    def control(self, x, y):
        """
        control player movement
        """
        self.rect.x += x
        self.rect.y += y



    def movement(self, pos=(0,0)):
        self.rect.x = pos[0]
        self.rect.y = pos[1]



    def update(self):

        self.current_sprite += 0.05  # aumente # de frames entre cada FPS
        if self.current_sprite > len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)-1] # si es entero cambiar frame


        self.vars['location'][0] = self.rect.x
        self.vars['location'][1] = self.rect.y
        # screen.blit(self.image, (self.rectn[0],self.rectn[1]))



class StoreBg(pygame.sprite.Sprite):
    '''Usar esta clase para colisionar '''
    def __init__(self, floor_image_surface, location=[0,0], store_id=1, multi=False): # Added floor_image_surface
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.image.load(asset('assets/img', 'floor.png')) # Removed direct loading
        self.image = floor_image_surface # Use the passed surface
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
    
    def movement(self, pos=(0,0)):
        self.rect.x = pos[0]
        self.rect.y = pos[1]+108

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