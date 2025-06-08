import pygame
from pygame.locals import *
from .pygamextras import *


class Menu:
    
    def __init__(self):
        # menu = Menu Item Player
        #
        self.w = int((W/100)*80)
        self.h = int((H/100)*80)
        self.menu = pygame.Surface((self.w, self.h))
        # menu_h_center, menu_w_center = menu.get_height()/2, menu.get_width()/2
        self.menu.get_rect()
        # menu.center
        self.menu.set_alpha(200)
        self.menu.fill('white')

    def show(self):
        # Dibujar el menu en medio
        screen.blit(self.menu, (((W//2)-self.w/2), ((H//2)-self.h/2)))


class Dialogue(Menu):
    def __init__(self):
        self.moving = [0, True]

    def show(self, position=[]):
        # Dialogues - exchange system
        if self.moving[0] < 10 and self.moving[1] == True:
            self.moving[0] += 1
            if self.moving[0] >= 10:
                self.moving[1] = False
        elif self.moving[1] == False and self.moving[0] <= 10:
            self.moving[0] -= 1
            if self.moving[0] <= -10:
                self.moving[1] = True
            
        # elif self.moving[0] > 100 and self.moving[1]:
        #     self.moving[1] = False
        
        pygame.draw.rect(screen, 'white', position, 0, 5)


class Button:
    def __init__(self, rect, text, font, text_color, button_color, hover_color, action=None):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.font = font
        self.text_color = text_color
        self.button_color = button_color
        self.hover_color = hover_color
        self.action = action
        self.is_hovered = False

    def draw(self, surface, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.is_hovered = True
            pygame.draw.rect(surface, self.hover_color, self.rect)
        else:
            self.is_hovered = False
            pygame.draw.rect(surface, self.button_color, self.rect)

        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.action:
                self.action()


class MenuManager:
    def __init__(self):
        self.buttons = []

    def add_button(self, rect, text, font, text_color, button_color, hover_color, action=None):
        button = Button(rect, text, font, text_color, button_color, hover_color, action)
        self.buttons.append(button)
        return button

    def draw(self, surface, mouse_pos):
        for button in self.buttons:
            button.draw(surface, mouse_pos)

    def handle_event(self, event):
        for button in self.buttons:
            button.handle_event(event)