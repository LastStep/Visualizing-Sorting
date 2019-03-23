import pygame as py
from random import randint
import numpy as np
py.init()

w = 800
h = 800
length = w//2

screen = py.display.set_mode((w,h))

values = [randint(0,h//2) for i in range(length)]
values = np.array([values])

a, b = 0, 0

def BubbleSort():
  global a, b
  for i in range(length):
    if b < length - a - 1:
      if values[0][b] > values[0][b + 1]:
        values[0][b], values[0][b + 1] = values[0][b + 1], values[0][b]
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

  BubbleSort()
  screen.fill((0,0,0))

  for x,i in enumerate(values[0][::-1]):
    py.draw.line(screen, (255,255,255), (x, h//2), (x,i))

  py.display.update()
  clock.tick(60)

py.quit()

