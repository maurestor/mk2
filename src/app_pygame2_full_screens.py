import sys
import pygame
from pygame.locals import *


class Text:
    """Create a text object."""

    def __init__(self, text, pos, **options):
        self.text = text
        self.pos = pos

        self.fontname = None
        self.fontsize = 50
        self.fontcolor = Color('black')
        self.set_font()
        self.render()

    def set_font(self):
        """Set the font from its name and size."""
        self.font = pygame.font.SysFont(self.fontname, self.fontsize)

    def render(self):
        """Render the text into an image"""
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos

    def draw(self):
        App.screen.blit(self.img, self.rect)


class App:
    """Create a single-window app with miltiple scenes."""

    def __init__(self):
        """Initialize pygame and application."""
        pygame.init()

        self.flags = RESIZABLE
        self.rect = Rect(0, 0, 800, 600)
        App.screen = pygame.display.set_mode(self.rect.size, self.flags)
        App.clock = pygame.time.Clock()

        App.tx = Text('Mercadi2', (20, 20))

        App.running = True

        self.shortcuts = {
            (K_x, 4097): 'print("shift+X")',
            (K_x, 4352): 'print("alt+X")',
            (K_x, 4160): 'print("ctrl+X")',

            (K_f, 4160): 'self.toggle_fullscreen()',
            (K_r, 4160): 'self.toggle_resizable()',
            (K_g, 4160): 'self.toggle_frame()',
            # (K_x, 4160 + 4097): 'print("ctl+shift+X")',
            # (K_x, 4160 + 4352): 'print("ctl+alt+X")',
            # (K_x, 4160 + 4097 + 4352): 'print("ctl+alt+shift+X")',
        }

    def toggle_fullscreen(self):
        """Toggle between full screen and windowed screen."""
        self.flags ^= FULLSCREEN
        pygame.display.set_mode((0, 0), self.flags)
        
    def toggle_resizable(self):
        """Toggle between resizable and fixed-size window."""
        self.flags ^= RESIZABLE
        pygame.display.set_mode(self.rect.size, self.flags)

    def toggle_frame(self):
        """Toggle between frame and noframe window."""
        self.flags ^= NOFRAME
        pygame.display.set_mode(self.rect.size, self.flags)


    def do_shortcut(self, event):
        """Find the the key/mod combination in the dicciotionary"""
        k = event.key
        m = event.mod
        # u = event.unicode
        if (k, m) in self.shortcuts:
            # print('entre')
            exec(self.shortcuts[k, m])


    def run(self):
        """Run the MAIN EVENT loop."""
        while App.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    App.running = 0
                elif event.type == KEYDOWN:
                    self.do_shortcut(event)
                    print(event)
                    if event.key == K_ESCAPE:
                        App.running = 0

            App.screen.fill('darkgray')

            App.tx.draw()

            App.clock.tick(60)
            pygame.display.update()
        pygame.quit()
        # sys.exit()


if __name__ == '__main__':
    App().run()
