import pygame
import time
from settings import *
from algorithms import *
from mainScreen import *
import random

pygame.init()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    click = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()

    selection.draw(mouse, "Selection Sort")
    bubble.draw(mouse, "Bubble Sort")
    gnome.draw(mouse, "Gnome Sort")

    if click[0] == 1:
        if selection.isOver(mouse):
            selectionSort(rectangles)
            pygame.quit()
        elif bubble.isOver(mouse):
            bubbleSort(rectangles)
            pygame.quit()
        elif gnome.isOver(mouse):
            gnomeSort(rectangles)
            pygame.quit()
        elif insertion.isOver(mouse):
            insertionSort(rectangles)
            pygame.quit()

    pygame.display.flip()
