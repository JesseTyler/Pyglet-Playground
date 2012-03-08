from __future__ import print_function

import pyglet, math
from pyglet.window import *

window = pyglet.window.Window(600,600)

tick = 0

keys = key.KeyStateHandler()
window.push_handlers(keys)

crate_img = pyglet.resource.image('img/crate.png')
s_Crate = pyglet.sprite.Sprite(crate_img)

@window.event
def on_draw():
    window.clear()
    s_Crate.draw()

def update(dt):
    global tick
    if tick == 30:
        tick = 0
    tick += 1
    print(tick)

    if keys[key.W]:
        if s_Crate.y + 5 > 560:
            return
        s_Crate.y += 5
        print('y: %d x: %d' % (s_Crate.y, s_Crate.x))

    if keys[key.S]:
        if s_Crate.y - 5 < 0:
            return
        s_Crate.y -= 5
        print('y: %d x: %d' % (s_Crate.y, s_Crate.x))

    if keys[key.A]:
        if s_Crate.x - 5 < 0:
            return
        s_Crate.x -= 5
        print('y: %d x: %d' % (s_Crate.y, s_Crate.x))

    if keys[key.D]:
        if s_Crate.x + 5 > 560:
            return
        s_Crate.x += 5
        print('y: %d x: %d' % (s_Crate.y, s_Crate.x))

pyglet.clock.schedule_interval(update, 1/30.)

pyglet.app.run()
