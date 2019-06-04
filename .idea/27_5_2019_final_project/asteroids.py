import random

import math
import pyglet
from pyglet import gl
from pyglet.window import key

ROTATION_SPEED = 4 
ACCELERATION = 30
ASTEROID_SPEED = 15

def load_image(path):
    image = pyglet.image.load(path)
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2
    return image


window = pyglet.window.Window()

pressed_keys = set()

batch = pyglet.graphics.Batch()

objects = []

asteroid_imgs = [load_image('.idea/27_5_2019_final_project/PNG/Meteors/meteorBrown_big1.png'),
            load_image('.idea/27_5_2019_final_project/PNG/Meteors/meteorGrey_big3.png'),
            load_image('.idea/27_5_2019_final_project/PNG/Meteors/meteorGrey_tiny1.png'),
            load_image('.idea/27_5_2019_final_project/PNG/Meteors/meteorBrown_small1.png') ]
ship_img = load_image('.idea/27_5_2019_final_project/PNG/playerShip1_blue.png')

def draw_circle(x, y, radius):
    iterations = 20
    s = math.sin(2*math.pi / iterations)
    c = math.cos(2*math.pi / iterations)

    dx, dy = radius, 0

    gl.glBegin(gl.GL_LINE_STRIP)
    for i in range(iterations+1):
        gl.glVertex2f(x+dx, y+dy)
        dx, dy = (dx*c - dy*s), (dy*c + dx*s)
    gl.glEnd()


def distance(a, b, wrap_size):
    """Distance in one dirextion (x or y)"""
    result = abs(a - b)
    if result > wrap_size / 2:
        result = wrap_size - result
    return result


def overlaps(a, b):
    """Returns true iff two space objects overlap"""
    distance_squared = (distance(a.x, b.x, window.width) ** 2 +
                        distance(a.y, b.y, window.height) ** 2)
    max_distance_squared = (a.radius + b.radius) ** 2
    return distance_squared < max_distance_squared
    
class SpaceObject:
    def __init__(self, window):
        self.x = window.width / 2 
        self.y = window.height / 2 
        self.x_speed = 50
        self.y_speed = 50
        self.rotation = 0
        self.rotation_speed = 0

    def draw(self):
        self.sprite.x = self.x
        self.sprite.y = self.y
        self.sprite.rotation = 90 - math.degrees(self.rotation)

    def tick(self, dt):
        distance_x = self.x_speed * dt
        distance_y = self.y_speed * dt
        self.x = self.x + distance_x
        self.y = self.y + distance_y
        self.rotation = self.rotation + self.rotation_speed * dt

        while self.x > window.width:
            self.x = self.x - window.width

        while self.x < 0:
            self.x = self.x + window.width

        while self.y > window.height:
            self.y = self.y - window.height
class Spaceship(SpaceObject):
    def __init__(self, window):
        super().__init__(window)
        self.sprite = pyglet.sprite.Sprite(ship_img, batch=batch)
        self.radius = 20
        
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

        draw_circle(self.x, self.y, self.radius)

        

        super().tick(dt)

class Asteroid(SpaceObject):
    def __init__(self, window):
        super().__init__(window)
        img = random.choice(asteroid_imgs)
        self.sprite = pyglet.sprite.Sprite(img, batch=batch)
        self.radius = 30

        if random.randrange(2) == 1:
            self.x = 0 + (img.width / 2)
            self.y = random.uniform(0 , window.height )
        else:
            self.x = random.uniform(0 , window.width )
            self.y = 0 + (img.width / 2)
        
        self.rotation_speed = random.uniform(-ROTATION_SPEED, ROTATION_SPEED)

        self.x_speed = random.uniform(-ASTEROID_SPEED, ASTEROID_SPEED)
        self.y_speed = random.uniform(-ASTEROID_SPEED, ASTEROID_SPEED)
        draw_circle(self.x, self.y, self.radius)

        

objects.append(Spaceship(window))
objects.append(Asteroid(window))
objects.append(Asteroid(window))
objects.append(Asteroid(window))
objects.append(Asteroid(window))



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

