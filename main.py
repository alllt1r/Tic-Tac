import pygame
import sys

FPS = 60
WIN_WIDTH = 300
WIN_HEIGHT = 300
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BR_GREY = (200, 200, 200)
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Tic-Tac')
f1 = pygame.font.SysFont('sans-serif', 35)
circle_diameter = 45
cross_width = 6
a = 1
c = False
pos = [None, None, None,
       None, None, None,
       None, None, None]


def draw_scene():
    pygame.draw.line(sc, BLACK, (100, 0), (100, 300), 5)
    pygame.draw.line(sc, BLACK, (200, 0), (200, 300), 5)
    pygame.draw.line(sc, BLACK, (0, 100), (300, 100), 5)
    pygame.draw.line(sc, BLACK, (0, 200), (300, 200), 5)


def win():
    if c == 1:
        pygame.draw.rect(sc, BLACK, (23, 131, 255, 34))
        sc.blit(f1.render("Player number 1 won", True, WHITE), (28, 135))
    if c == 0:
        pygame.draw.rect(sc, BLACK, (23, 131, 255, 34))
        sc.blit(f1.render("Player number 2 won", True, WHITE), (28, 135))


def draw():
    pygame.draw.rect(sc, BLACK, (82, 131, 140, 34))
    sc.blit(f1.render("It is a draw", True, WHITE), (87, 135))


run = True
isEnd = False
while run:
    sc.fill(WHITE)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if i.type == pygame.MOUSEBUTTONDOWN and a != 0 and pos[a - 1] == None and isEnd == False:
            c = not c
            pos[a - 1] = int(c)

    # print(a)
    print(f"{pos[0], pos[1], pos[2]}\n{pos[3], pos[4], pos[5]}\n{pos[6], pos[7], pos[8]}\n")

    draw_scene()
    mouse = pygame.mouse.get_pos()
    if isEnd == False:
        if 5 < mouse[0] < 95:
            if 5 < mouse[1] < 95 and pos[0] == None:
                pygame.draw.rect(sc, BR_GREY, (5, 5, 90, 90))
                a = 1
            if 105 < mouse[1] < 195 and pos[3] == None:
                pygame.draw.rect(sc, BR_GREY, (5, 105, 90, 90))
                a = 4
            if 205 < mouse[1] < 295 and pos[6] == None:
                pygame.draw.rect(sc, BR_GREY, (5, 205, 90, 90))
                a = 7
        elif 105 < mouse[0] < 195:
            if 5 < mouse[1] < 95 and pos[1] == None:
                pygame.draw.rect(sc, BR_GREY, (105, 5, 90, 90))
                a = 2
            if 105 < mouse[1] < 195 and pos[4] == None:
                pygame.draw.rect(sc, BR_GREY, (105, 105, 90, 90))
                a = 5
            if 205 < mouse[1] < 295 and pos[7] == None:
                pygame.draw.rect(sc, BR_GREY, (105, 205, 90, 90))
                a = 8
        elif 205 < mouse[0] < 295:
            if 5 < mouse[1] < 95 and pos[2] == None:
                pygame.draw.rect(sc, BR_GREY, (205, 5, 90, 90))
                a = 3
            if 105 < mouse[1] < 195 and pos[5] == None:
                pygame.draw.rect(sc, BR_GREY, (205, 105, 90, 90))
                a = 6
            if 205 < mouse[1] < 295 and pos[8] == None:
                pygame.draw.rect(sc, BR_GREY, (205, 205, 90, 90))
                a = 9
        else:
            a = 0

    if pos[0] == 1:
        pygame.draw.line(sc, BLACK, (5, 5), (95, 95), cross_width)
        pygame.draw.line(sc, BLACK, (95, 5), (5, 95), cross_width)
    elif pos[0] == 0:
        pygame.draw.circle(sc, BLACK, (50, 50), circle_diameter, 5)
    if pos[1] == 1:
        pygame.draw.line(sc, BLACK, (105, 5), (195, 95), cross_width)
        pygame.draw.line(sc, BLACK, (195, 5), (105, 95), cross_width)
    elif pos[1] == 0:
        pygame.draw.circle(sc, BLACK, (150, 50), circle_diameter, 5)
    if pos[2] == 1:
        pygame.draw.line(sc, BLACK, (205, 5), (295, 95), cross_width)
        pygame.draw.line(sc, BLACK, (205, 95), (295, 5), cross_width)
    elif pos[2] == 0:
        pygame.draw.circle(sc, BLACK, (250, 50), circle_diameter, 5)
    if pos[3] == 1:
        pygame.draw.line(sc, BLACK, (5, 105), (95, 195), cross_width)
        pygame.draw.line(sc, BLACK, (95, 105), (5, 195), cross_width)
    elif pos[3] == 0:
        pygame.draw.circle(sc, BLACK, (50, 150), circle_diameter, 5)
    if pos[4] == 1:
        pygame.draw.line(sc, BLACK, (105, 105), (195, 195), cross_width)
        pygame.draw.line(sc, BLACK, (195, 105), (105, 195), cross_width)
    elif pos[4] == 0:
        pygame.draw.circle(sc, BLACK, (150, 150), circle_diameter, 5)
    if pos[5] == 1:
        pygame.draw.line(sc, BLACK, (205, 105), (295, 195), cross_width)
        pygame.draw.line(sc, BLACK, (205, 195), (295, 105), cross_width)
    elif pos[5] == 0:
        pygame.draw.circle(sc, BLACK, (250, 150), circle_diameter, 5)
    if pos[6] == 1:
        pygame.draw.line(sc, BLACK, (5, 205), (95, 295), cross_width)
        pygame.draw.line(sc, BLACK, (95, 205), (5, 295), cross_width)
    elif pos[6] == 0:
        pygame.draw.circle(sc, BLACK, (50, 250), circle_diameter, 5)
    if pos[7] == 1:
        pygame.draw.line(sc, BLACK, (105, 205), (195, 295), cross_width)
        pygame.draw.line(sc, BLACK, (195, 205), (105, 295), cross_width)
    elif pos[7] == 0:
        pygame.draw.circle(sc, BLACK, (150, 250), circle_diameter, 5)
    if pos[8] == 1:
        pygame.draw.line(sc, BLACK, (205, 205), (295, 295), cross_width)
        pygame.draw.line(sc, BLACK, (205, 295), (295, 205), cross_width)
    elif pos[8] == 0:
        pygame.draw.circle(sc, BLACK, (250, 250), circle_diameter, 5)

    if ((pos[0] == pos[1] == pos[2] != None) or (pos[3] == pos[4] == pos[5] != None) or (
            pos[6] == pos[7] == pos[8] != None) or (pos[0] == pos[3] == pos[6] != None) or (
            pos[1] == pos[4] == pos[7] != None) or (pos[2] == pos[5] == pos[8] != None) or (
            pos[6] == pos[4] == pos[2] != None) or (pos[0] == pos[4] == pos[8] != None)):
        win()
        isEnd = True
    if not None in pos:
        draw()
        isEnd = True

    pygame.display.update()
    clock.tick(FPS)    