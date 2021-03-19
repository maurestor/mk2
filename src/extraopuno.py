import os

class ExtraOpUno:
    ''' Extra optional Uno '''
    def __init__(self):
        x = 100
        y = 0
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
        print('Modulo {} importado'.format(x))

if __name__ == '__main__':
    ExtraOpUno()