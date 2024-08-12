import pygame
import random

width = 500
height = 500

black = (0, 0, 0)
white = (255, 255, 255)
grey = (150, 150, 150)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

screen = pygame.display.set_mode((width, height))

rectangles = []
rectangles2 = []
for i in range(125):
    rectangles.append(random.randrange(1, 500))
    rectangles2.append(random.randrange(1, 500))


def sort(array):
    temp = 0
    for x in range(len(array)):
        minIndex = x
        for y in range(x + 1, len(array)):
            if array[minIndex] > array[y]:
                minIndex = y
        temp = array[x]
        array[x] = array[minIndex]
        array[minIndex] = temp


class Button():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

    def draw(self, pos, text):
        font = pygame.font.SysFont('comicsans', 50)
        writing = font.render(text, 1, white)

        if self.isOver(pos):
            pygame.draw.rect(
                screen, grey, (self.x, self.y, self.width, self.height))
            screen.blit(writing, (self.x + (self.width / 2) - 100,
                                  self.y + (self.height / 2)))
        else:
            pygame.draw.rect(
                screen, black, (self.x, self.y, self.width, self.height))


selection = Button(0, 0, 250, 250)
bubble = Button(250, 0, 250, 250)
gnome = Button(0, 250, 250, 250)
insertion = Button(250, 250, 250, 250)
