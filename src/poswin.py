import os

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

    def pos_win(self):
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (self.x, self.y)
        # print('Modulo {} importado'.format(self.x))

pos_win = PosWin().pos_win()

if __name__ == '__main__':
    PosWin()