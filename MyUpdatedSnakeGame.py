import pygame as pg
import random as rd
from enum import Enum
from collections import namedtuple

pg.init()

class Direction(Enum):
  RIGHT = 1
  LEFT= 2
  UP = 3
  DOWN = 4

Point = namedtuple("Point", "x, y")

BLACK = (0,0,0)
GREEN1 = (127,255,0)
GREEN2 = (69,139,0)
BLUE = (0,0,255)
WHITE = (240,255,255)


SIZE_BLOCK = 20
SNAKESPEED = 20
class snakeGame:

  def __init__(self, w=640, h=480):
    self.w = w
    self.h = h

    self.display = pg.display.set_mode((self.w, self.h))
    pg.display.set_caption("Snake")
    self.clock = pg.time.Clock()


    self.direction = Direction.RIGHT

    self.head = Point(self.w/2, self.h/2)
    self.snake = [self.head, Point(self.head.x-SIZE_BLOCK, self.head.y), Point(self.head.x-(2*SIZE_BLOCK), self.head.y)]

    self.score = 0
    self.food = None
    self._place_food()

  def _place_food(self):
    x = rd.randint(0, (self.w-SIZE_BLOCK)//SIZE_BLOCK)*SIZE_BLOCK
    y = rd.randint(0, (self.h-SIZE_BLOCK)//SIZE_BLOCK)*SIZE_BLOCK
    self.food = Point(x, y)
    if self.food in self.snake:
      self._place_food()

  def start_step(self):









    self.updateMyUi()
    self.clock.tick(SNAKESPEED)

    endOfGame = False
    return endOfGame, self.score

  def updateMyUi(self):
    self.display.fill(BLACK)



if __name__ == "__main__":
  myGame = snakeGame()

  while True:
    endOfGame, score = myGame.start_step()

    if endOfGame == True:
      break

  print("Your final score is;", score)



  pg.quit()

