import pygame
from random import randrange
pygame.init()

HEIGHT = 600
WIDTH = 800
GREEN = 144, 230, 92
RED = 235, 64, 40

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
def draw_list(list,num_blocks, red, green, algo):
    block_width = ((WIDTH-40)/num_blocks)
    # looping through block heights and calculating coordinates for each block to be drawn
    window.fill((0,0,0))

    title = pygame.font.SysFont('Ariel', 40).render(f"Current Sort: {algo}", 200, GREEN)
    insert = pygame.font.SysFont('Ariel', 40).render("Insertion Sort - 'I'", 200, GREEN)
    select = pygame.font.SysFont('Ariel', 40).render("Selection Sort - 'S'", 200, GREEN)
    start = pygame.font.SysFont('Ariel', 40).render("Start Sorting - Space", 200, GREEN)
    reset = pygame.font.SysFont('Ariel', 40).render("Reset List - 'r''", 200, GREEN)

    window.blit(title, (HEIGHT/2 - title.get_width()/4, 20))
    window.blit(insert, (10, 70))
    window.blit(select, (10, 110))
    window.blit(reset, (10, 150))
    window.blit(start, (10, 190))



    for count, i in enumerate(list.lst):
        rect = pygame.Rect(20 + count * block_width, HEIGHT - i, block_width, i)
        if count == green:
            pygame.draw.rect(window, GREEN, rect)
        elif count == red:
            pygame.draw.rect(window, RED, rect)
        elif red == -1 or green == -1:
            pygame.draw.rect(window, (count * 10, 100, 255), rect)
        else:
            pygame.draw.rect(window, (count * 10, 100, 255), rect)
    pygame.display.update()

def insertionSort(list, num_elements):
    clock = pygame.time.Clock()
    for i in range(1, len(list.lst)): 
        clock.tick(20)
        key = list.lst[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        
        while j >=0 and key < list.lst[j] :
                clock.tick(20)
                list.lst[j+1] = list.lst[j]
                draw_list(list, num_elements, i, j, "Insertion Sort")
                j -= 1
        list.lst[j+1] = key
        draw_list(list, num_elements, i, j, "Insertion Sort")
    
def selectionSort(list, num_elements):
    clock = pygame.time.Clock()
    for i in range(len(list.lst)):
        # Find the minimum element in remaining 
        # unsorted array
        clock.tick(10)
        min_idx = i
        for j in range(i+1, len(list.lst)):
            clock.tick(10)
            draw_list(list, num_elements, i, j, "Selection Sort")
            if list.lst[min_idx] > list.lst[j]:
                min_idx = j
              
        # Swap the found minimum element with 
        # the first element        
        list.lst[i], list.lst[min_idx] = list.lst[min_idx], list.lst[i]
        draw_list(list, num_elements, i, j, "Selection Sort")

def sorting(sort, lst, num_elements):
    if sort == 'Insertion Sort':
        insertionSort(lst,num_elements)
    if sort == 'Selection Sort':
        selectionSort(lst,num_elements)
# game loop
def main():
    run = True
    num_elements = 20
    lst = List(num_elements)
    sort = 'Insertion Sort'
    draw_list(lst, num_elements, -1, -1, sort)
    while run:
        for event in pygame.event.get():
            if event.type ==  pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    lst.lst = []
                    lst.generateList(num_elements)
                    draw_list(lst, num_elements, -1, -1, sort)
                elif event.key == pygame.K_SPACE:
                    sorting(sort, lst, num_elements)
                elif event.key == pygame.K_i:
                    sort = 'Insertion Sort'
                elif event.key == pygame.K_s:
                    sort = 'Selection Sort'
            draw_list(lst, num_elements, -1, -1, sort)



if __name__ == '__main__':
    main()
pygame.quit()

