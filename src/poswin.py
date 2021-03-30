import os
import random

class PosWin:
    '''Establece la ubicacion fija de la ventana en el escritorio.

    Los valore definidos son:
    horizontal = x = 0
    vertical = y = 30
    
    Tomando en cuenta que los valores inciales se cuentan desde:
    Derecha a izquierda en el eje X.
    Arriba hacia abajo en el eje Y.

    '''
    def __init__(self, x=0, y=30):
        self.x = x
        self.y = y
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (self.x, self.y)


    def pos_rand(self, rx=0, ry=30):
        # print('Modulo {} importado'.format(self.x))
        self.rx = random.randint(0, rx)
        self.ry = random.randint(30, ry)
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (self.rx, self.ry)


if __name__ == '__main__':
    PosWin()