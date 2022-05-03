import pygame as pg
import random as rd
from enum import Enum
from collections import namedtuple

from pyparsing import Or

pg.init()
gameFont = pg.font.Font("QUICKENS.ttf", 30)

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
SNAKESPEED = 10
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

    for i in pg.event.get():
      if i.type == pg.QUIT:
        pg.QUIT()
        quit()
      if i.type == pg.KEYDOWN:
        if i.key == pg.K_LEFT:
          self.direction = Direction.LEFT
        elif i.key == pg.K_RIGHT:
          self.direction = Direction.RIGHT
        elif i.key == pg.K_UP:
          self.direction = Direction.UP
        elif i.key == pg.K_DOWN:
          self.direction = Direction.DOWN

    self._move(self.direction)
    self.snake.insert(0, self.head)

    
    endOfGame = False
    if self.collision():
      endOfGame = True
      return endOfGame, self.score

    if self.head == self.food:
      self.score += 1
      self._place_food()
    else:
      self.snake.pop()


    self.updateMyUi()
    self.clock.tick(SNAKESPEED)

    
    return endOfGame, self.score

  def collision(self):
    if self.head.x > self.w - SIZE_BLOCK or self.head.x < 0 or self.head.y > self.h - SIZE_BLOCK or self.head.y < 0:
      return True

    if self.head in self.snake[1:]:
      return True

    return False

  def updateMyUi(self):
    self.display.fill(BLACK)

    for i in self.snake:
      pg.draw.rect(self.display, GREEN1, pg.Rect(i.x, i.y, SIZE_BLOCK, SIZE_BLOCK))
      pg.draw.rect(self.display, GREEN2, pg.Rect(i.x+4, i.y+4, 11, 11))

    pg.draw.rect(self.display, BLUE, pg.Rect(self.food.x, self.food.y, SIZE_BLOCK, SIZE_BLOCK))

    myText = gameFont.render("Score: " + str(self.score), True, WHITE)
    self.display.blit(myText, [0,0])
    pg.display.flip()

  def _move(self, direction):
    x = self.head.x
    y = self.head.y
    if direction == Direction.RIGHT:
      x += SIZE_BLOCK
    elif direction == Direction.LEFT:
      x -= SIZE_BLOCK
    elif direction == Direction.DOWN:
      y += SIZE_BLOCK
    elif direction == Direction.UP:
      y -= SIZE_BLOCK

    self.head = Point(x,y)

if __name__ == "__main__":
  myGame = snakeGame()

  while True:
    endOfGame, score = myGame.start_step()

    if endOfGame == True:
      break

  print("Your final score is;", score)

  pg.quit()

