import pygame
import time
from settings import *
from algorithms import *
import random


def mainScreen():
    drawScreen(rectangles2)
    time.sleep(0.5)
    screen.fill(black)
    sort(rectangles)
    drawScreen(rectangles)
    time.sleep(0.5)
    screen.fill(black)
