from cmath import rect
import pygame
from random import randrange
pygame.init()

HEIGHT = 600
WIDTH = 800

window = pygame.display.set_mode((WIDTH, HEIGHT))


# list of blocks that will be sorted
class List:
    def generateList(self, num_blocks):
        for i in range(num_blocks):
            height = randrange(300) + 20
            self.lst.append(height)

    def __init__(self, size):
        self.lst = []
        self.generateList(size)



def draw_list(list,num_blocks):
    block_width = ((WIDTH-40)/num_blocks)
    rectangle_lst = []
    # looping through block heights and calculating coordinates for each block to be drawn

    for count, i in enumerate(list.lst):
        rect = pygame.Rect(20 + count * block_width, HEIGHT - i, block_width, i)
        pygame.draw.rect(window, (255, 100, 255), rect)

    pygame.display.update()



def main():
    run = True
    num_elements = 500
    lst = List(num_elements)
    while run:
        for event in pygame.event.get():
            if event.type ==  pygame.QUIT:
                run = False
            draw_list(lst, num_elements)


main()

pygame.quit()

