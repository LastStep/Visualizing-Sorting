import pygame as py
import math
import numpy as np
from random import randint
py.init()

w = 765
h = 600
lineh = h - 300
radius = 200
center = [w//2,h//2]
angle = (2*math.pi)/w

screen = py.display.set_mode((w,h))

# def LumiValue(r,g,b):
#   return 0.299*r + 0.587*g + 0.114*b

def HueValue(r,g,b):
  MAX = max(r,g,b)
  MIN = min(r,g,b)
  temp = MAX-MIN
  if temp == 0:
    return 0
  elif MAX == r:
    return abs(b-g)/temp
  elif MAX == g:
    return 2 + abs(r-b)/temp
  else:
    return 4 + abs(r-g)/temp

colors = []
for i in range(w):
  colors.append((randint(0,255),randint(0,255),randint(0,255)))
HueValues = [HueValue(*i) for i in colors]
lenght = [randint(50,300) for i in range(w)]
values = np.array([HueValues,colors,lenght])

a, b = 0, 0

def Sort():
  global a, b
  for i in range(w):
    if b < w - a - 1:
      if values[0][b] > values[0][b + 1]:
        values[0][b], values[0][b + 1] = values[0][b + 1], values[0][b]
        values[1][b], values[1][b + 1] = values[1][b + 1], values[1][b]
        values[2][b], values[2][b + 1] = values[2][b + 1], values[2][b]
      b += 1
    else:
      a += 1
      b = 0

clock = py.time.Clock()

game = True
while game:
  # py.time.delay(50)
  for event in py.event.get():
    if event.type == py.QUIT:
      game = False

  Sort()

  screen.fill((255,255,255))

  for k,i in enumerate(values[1]):
    x = center[0] + math.sin(k*angle) * values[2][k]
    y = center[1] + math.cos(k*angle) * values[2][k]
    py.draw.line(screen, i, center, [x,y])

  py.display.update()
  clock.tick(60)

py.quit()

