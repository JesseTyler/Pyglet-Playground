from __future__ import print_function

import pyglet
from pyglet.window import *

window = pyglet.window.Window()
image = pyglet.resource.image('img/crate.png')

image_x = 0
image_y = 0

@window.event
def on_key_press(symbol, modifiers):
    global image_x, image_y
    if symbol == key.W:
        if image_y + 40 > 440:
            return
        image_y += 40
        print('y: %d x: %d' % (image_y, image_x))
    elif symbol == key.S:
        if image_y - 40 < 0:
            return
        image_y -= 40
        print('y: %d x: %d' % (image_y, image_x))
    elif symbol == key.A:
        if image_x - 40 < 0:
            return
        image_x -= 40
        print('y: %d x: %d' % (image_y, image_x))
    elif symbol == key.D:
        if image_x + 40 > 600:
            return
        image_x += 40
        print('y: %d x: %d' % (image_y, image_x))
                          
@window.event
def on_draw():
    global image_x, image_y
    window.clear()
    image.blit(image_x, image_y)
    
pyglet.app.run()
