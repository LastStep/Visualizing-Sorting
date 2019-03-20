import pygame as py
from random import randint
import numpy as np
py.init()

w = 765
h = 600
screen = py.display.set_mode((w,h))

color1, color2, color3 = [], [], []
for i in range(256):
  color1.append((i,0,0))
  color2.append((0,i,0))
  color3.append((0,0,i))
colors = color1+color2+color3
values = [randint(h-500,h) for i in range(w)]
values = np.array([values,colors])

a, b = 0, 0

def Sort():
  global a, b
  for i in range(w):
    if b < w - a - 1:
      if values[0][b] > values[0][b + 1]:
        values[0][b], values[0][b + 1] = values[0][b + 1], values[0][b]
     #   values[1][b], values[1][b + 1] = values[1][b + 1], values[1][b]

      b += 1
    else:
      a += 1
      b = 0

clock = py.time.Clock()

game = True
while game:
  # py.time.delay(100)

  for event in py.event.get():
    if event.type == py.QUIT:
      game = False

  Sort()
  screen.fill((0,0,0))

  for x,i in enumerate(values[0][::-1]):
    py.draw.line(screen, values[1][x], (x, h), (x,i))

  py.display.update()
  clock.tick(60)

py.quit()

