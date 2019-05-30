import random

import math
import pyglet
from pyglet import gl
from pyglet.window import key

ROTATION_SPEED = 4 
ACCELERATION = 30

def load_image(path):
    image = pyglet.image.load(path)
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2
    return image


window = pyglet.window.Window()

pressed_keys = set()

batch = pyglet.graphics.Batch()

objects = []

ship_img = load_image('.idea/27_5_2019_final_project/PNG/playerShip1_blue.png')

class Spaceship:
    def __init__(self, window):
        self.x = window.width / 2 
        self.y = window.height / 2 
        self.x_speed = 100
        self.y_speed = 100
        self.rotation = 0
        self.sprite = pyglet.sprite.Sprite(ship_img, batch=batch)

    def draw(self):
        self.sprite.x = self.x
        self.sprite.y = self.y
        self.sprite.rotation = 90 - math.degrees(self.rotation)

    def tick(self, dt):
        if pyglet.window.key.LEFT in pressed_keys:
            self.rotation = self.rotation - ROTATION_SPEED * dt
        if pyglet.window.key.RIGHT in pressed_keys:
            self.rotation = self.rotation + ROTATION_SPEED * dt
        if pyglet.window.key.UP in pressed_keys:
            rot = math.radians(self.rotation)
            self.x = self.x + dt * self.x_speed
            self.y = self.y + dt * self.y_speed
        if pyglet.window.key.DOWN in pressed_keys:
            rot = math.radians(self.rotation)
            self.x = self.x - dt * self.x_speed
            self.y = self.y - dt * self.y_speed

       
        
        

        while self.x > window.width:
            self.x = self.x - window.width

        while self.x < 0:
            self.x = self.x + window.width

        while self.y > window.height:
            self.y = self.y - window.height


objects.append(Spaceship(window))



def draw():
    window.clear()

    for x_offset in (-window.width, 0, window.width):
        for y_offset in (-window.height, 0, window.height):
            # Remember the current state
            gl.glPushMatrix()
            # Move everything drawn from now on by (x_offset, y_offset, 0)
            gl.glTranslatef(x_offset, y_offset, 0)

            # Draw
            for obj in objects:
                obj.draw()
            batch.draw()

            # Restore remembered state (this cancels the glTranslatef)
            gl.glPopMatrix()

def key_pressed(key, mod):
    pressed_keys.add(key)

def key_released(key,mod):
    pressed_keys.discard(key)



def tick(dt):
    for obj in objects:
        obj.tick(dt)


window.push_handlers(on_draw=draw, on_key_press=key_pressed, on_key_release=key_released)

pyglet.clock.schedule_interval(tick, 1 / 30)

pyglet.app.run()

