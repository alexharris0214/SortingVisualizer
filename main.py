from cmath import rect
import pygame
from random import randrange
pygame.init()

HEIGHT = 600
WIDTH = 800
GREEN = 0, 255, 0
RED = 255, 0, 0

window = pygame.display.set_mode((WIDTH, HEIGHT))


# list of blocks that will be sorted
class List:
    # randomly generates list of different heights
    def generateList(self, num_blocks):
        for i in range(num_blocks):
            height = randrange(300)
            self.lst.append(height)

    def __init__(self, size):
        self.lst = []
        self.generateList(size)

# draws the list of rectangles at its curretnt state with what values should be red and green
def draw_list(list,num_blocks, red, green):
    block_width = ((WIDTH-40)/num_blocks)
    # looping through block heights and calculating coordinates for each block to be drawn
    window.fill((0,0,0))
    for count, i in enumerate(list.lst):
        rect = pygame.Rect(20 + count * block_width, HEIGHT - i, block_width, i)
        # if count == green:
        #     pygame.draw.rect(window, GREEN, rect)
        # elif count == red:
        #     pygame.draw.rect(window, RED, rect)
        # else:
        pygame.draw.rect(window, (count * 2, 100, 255), rect)
    pygame.display.update()

def insertionSort(list):
    clock = pygame.time.Clock()
    for i in range(1, len(list.lst)): 
        clock.tick(5)
        key = list.lst[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        
        while j >=0 and key < list.lst[j] :
                clock.tick(5)
                list.lst[j+1] = list.lst[j]
                draw_list(list, 100, 3, 9)
                j -= 1
        list.lst[j+1] = key
        draw_list(list, 100, 3, 9)

# game loop
def main():
    run = True
    num_elements = 100
    lst = List(num_elements)
    while run:
        for event in pygame.event.get():
            if event.type ==  pygame.QUIT:
                run = False
        draw_list(lst, num_elements, 4, 12)
        insertionSort(lst)

if __name__ == '__main__':
    main()
pygame.quit()

