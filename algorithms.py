import pygame
import time
from settings import *
import random
test = []
for i in range(10):
    test.append(random.randrange(1, 10))


def drawScreen(array):
    for i in range(125):
        pygame.draw.rect(
            screen, white, (i * 4, (500 - array[i]), 4, array[i]))
        pygame.draw.rect(
            screen, black, (i * 4, (500 - array[i]), 4, array[i]), 1)
    pygame.display.flip()


def bubbleSort(array):
    temp = 0
    screen.fill(black)
    drawScreen(rectangles)
    time.sleep(2)
    for i in range(len(array)):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

            screen.fill(black)
            drawScreen(rectangles)
            pygame.display.flip()
    time.sleep(2)


def selectionSort(array):
    temp = 0
    screen.fill(black)
    drawScreen(rectangles)
    time.sleep(2)
    for x in range(len(array)):
        minIndex = x
        for y in range(x + 1, len(array)):
            if array[minIndex] > array[y]:
                minIndex = y
        temp = array[x]
        array[x] = array[minIndex]
        array[minIndex] = temp

        screen.fill(black)
        drawScreen(rectangles)
        pygame.display.flip()
        time.sleep(0.1)
    time.sleep(2)


def gnomeSort(array):
    temp = 0
    n = len(array)
    index = 1
    screen.fill(black)
    drawScreen(rectangles)
    time.sleep(2)
    while index < n:
        if index == 0:
            index += 1
        elif array[index] >= array[index - 1]:
            index += 1
        elif array[index] < array[index - 1]:
            temp = array[index - 1]
            array[index - 1] = array[index]
            array[index] = temp
            index -= 1
        screen.fill(black)
        drawScreen(rectangles)
        pygame.display.flip()
    time.sleep(2)


def doubleSelectionSort(array):
    temp = 0
    screen.fill(black)
    drawScreen(rectangles)
    time.sleep(2)
    n = len(array)
    for x in range(n):
        minIndex = x
        maxIndex = x
        for y in range(x + 1, len(array) - x):
            if array[minIndex] > array[y]:
                minIndex = y
            elif array[maxIndex] < array[y]:
                maxIndex = y
        temp = array[x]
        array[x] = array[minIndex]
        array[minIndex] = temp

        temp = array[n - x - 1]
        array[n - x - 1] = array[maxIndex]
        array[maxIndex] = temp

        screen.fill(black)
        drawScreen(rectangles)
        pygame.display.flip()
        time.sleep(0.1)
    time.sleep(2)


def insertionSort(array):
    screen.fill(black)
    drawScreen(rectangles)
    time.sleep(2)
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
        screen.fill(black)
        drawScreen(rectangles)
        pygame.display.flip()
        time.sleep(0.1)
