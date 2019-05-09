import pyglet
import math

window= pyglet.window.Window()

def tik(t):
    had.x = had.x + t *20
    had.y = 20 + 20 * math.sin(had.x)


#pyglet.clock.schedule_interval(tik,1/30)

def zpracuj_text(text):
    had.x = 150
    had.rotation = had.rotation + 10


obrazek = pyglet.image.load('D:\Programovani\Python - pyladies\Soubory\had.png')
had = pyglet.sprite.Sprite(obrazek)
obrazek2 = pyglet.image.load('D:\Programovani\Python - pyladies\Soubory\had2.png')


def vykresli():
    window.clear()
    had.draw()

def zmen(t):
    had.image = obrazek2
    pyglet.clock.schedule_once(zmen_zpatky,0.3)

def zmen_zpatky(t):
    had.image = obrazek
    pyglet.clock.schedule_once(zmen,0.3)

pyglet.clock.schedule_once(zmen,1)


def klik (x,y, tlacitko, mod):
    had.x = x
    had.y = y

window.push_handlers(on_text=zpracuj_text,on_draw=vykresli,on_mouse_press=klik)

pyglet.app.run()
