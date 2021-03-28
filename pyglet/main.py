import pyglet

window = pyglet.window.Window(800, 600)



@window.event
def on_draw():
    window.clear()




if __name__ == '__main__':
    pyglet.app.run()

