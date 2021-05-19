import pygame
import random

class Actor(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = image
        self.pos = pygame.Vector2(pos)
        self.rect = self.image.get_rect(midbottom=self.pos)

    # def update(self, events, dt, p_vel):
    #     pass

class Player(Actor):
    def __init__(self, image, pos):
        super().__init__(image, pos)

    def update(self, events, dt, p_vel, screen):
        pressed = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        mousepos = pygame.mouse.get_pos()
        mouserel = pygame.mouse.get_rel()
        move = pygame.Vector2((0, 0))
        if pressed[pygame.K_w] or pressed[pygame.K_UP]: move += (0, -p_vel)
        if pressed[pygame.K_a] or pressed[pygame.K_LEFT]: move += (-p_vel, 0)
        if pressed[pygame.K_s] or pressed[pygame.K_DOWN]: move += (0, p_vel)
        if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]: move += (p_vel, 0)
        # elif mouse[0] and moving:
        #     if self.rect.collidepoint(mousepos):
        #         move += (pygame.mouse.get_rel())
        #         # move += 
        pygame.draw.rect(screen, 'gold', self.rect, 1)

        if move.length() > 0:
            move.normalize_ip()
        self.pos += move*(dt/5)
        print(self.pos, move, dt)
        self.rect.midbottom = self.pos
        
        if self.rect.collidepoint(mousepos):
            if mouse[0]:
                moving = True
                if moving:
                    mouse = pygame.Vector2(mousepos)
                    self.pos = mouse
                #     diferencia_arrastre_inicial = (mouse[0] - self.rect.x, 
                #                                   mouse[1] - self.rect.y)
                # diferencia_arrastre_actual = (mouse[0] - self.rect.x,
                #                             mouse[1] - self.rect.y)
                # ajuste_requerido = (diferencia_arrastre_actual[0]-diferencia_arrastre_inicial[0],                   diferencia_arrastre_actual[1]-diferencia_arrastre_inicial[1])
        elif mouse[0] == False:
            moving = False


class YAwareGroup(pygame.sprite.Group):
    def by_y(self, spr):
        return spr.pos.y

    def draw(self, surface):
        sprites = self.sprites()
        surface_blit = surface.blit
        for spr in sorted(sprites, key=self.by_y):
            self.spritedict[spr] = surface_blit(spr.image, spr.rect)
        self.lostsprites = []


def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    clock = pygame.time.Clock()
    dt = 1
    p_vel = 5

    moving = False

    
    sprites = YAwareGroup(
        Player(pygame.image.load('/home/restor/Documents/game-develop/Python manuals/player.old.png').convert_alpha(), (100, 200)), 
        Actor(pygame.image.load("/home/restor/Documents/game-develop/Python manuals/player.old.png").convert_alpha(), (200,200)) 
        )

    while True:
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                return
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    return

            print(e)


        screen.fill('gray20')

        sprites.update(events, dt, p_vel, screen)
        sprites.draw(screen)

        pygame.display.update()
        dt = clock.tick(60)

if __name__ == '__main__':
    main()