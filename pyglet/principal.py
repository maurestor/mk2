import pyglet
from pyglet.window import key
from pyglet.window import mouse
from pyglet.window import gl
"""
Fuentes propuestas:
        Nokia
        Comicoro
        pf tempesta seven
        retroville
        retrogaming
"""
window = pyglet.window.Window(width=640, height=480, caption='Nueva ventanilla')

a = [0]

image = pyglet.resource.image('img/png/player.png')


label = pyglet.text.Label('Juego Principal {}'.format(a[0]), 
                           font_name = 'arial',
                           font_size = 12,
                           color=(255, 255, 255, 255),
                           x = window.width // 2,
                           y = window.height // 2,
                           anchor_x = 'center',
                           anchor_y = 'center',
                           )
@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print('Se dio click en x{}, y{}',format(str(x), str(y)))


# Detecta teclado              
@window.event
def on_key_press(symbol, modifiers):
    global a
    tecla = ''
    if symbol == key.A:
        tecla = ', con la tecla A'
    elif symbol == key.LEFT:
        tecla = ', con la tecla \'izquierda\''
    elif symbol == key.ENTER:
        tecla = ', con la tecla ENTER'
    
    a[0] += 1
    print('Presione {} veces el teclado'.format(a[0]) + tecla + '.')

    

@window.event
def on_draw():
    window.clear()
    image.blit(100, 200)
    label.draw()
    pyglet.graphics.draw(2, pyglet.gl.GL_POINTS, ('v2i', (10, 15, 30, 35)))

# music = pyglet.resource.media('music/free_dave.mp3', streaming=False)
# music.play()

event_logger = pyglet.window.event.WindowEventLogger()
window.push_handlers(event_logger)

pyglet.app.run()