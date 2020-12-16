import pygame
import sys

TEAL = (0, 128, 128)
LINE = (0, 100, 100)
WHITE = (240, 240, 240)
BLACK = (30, 30, 30)

xOxList = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
isFull = [False, False, False, False, False, False, False, False, False]

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('XOX')
screen.fill(TEAL)


def drawing_lines():
    pygame.draw.line(screen, LINE, (0, 200), (600, 200), 8)
    pygame.draw.line(screen, LINE, (0, 400), (600, 400), 8)
    pygame.draw.line(screen, LINE, (200, 0), (200, 600), 8)
    pygame.draw.line(screen, LINE, (400, 0), (400, 600), 8)


def player1(pos_x, pos_y):
    # Birinci sütun
    global counter
    if pos_x <= 190 and pos_y <= 190 and not isFull[0]:
        pygame.draw.line(screen, WHITE, (35, 35), (160, 160), 8)
        pygame.draw.line(screen, WHITE, (160, 35), (35, 160), 8)
        xOxList[0] = 'X'
        isFull[0] = True
        counter += 1
    if pos_x <= 190 and (190 < pos_y < 380) and not isFull[1]:
        pygame.draw.line(screen, WHITE, (35, 240), (160, 365), 8)
        pygame.draw.line(screen, WHITE, (160, 240), (35, 365), 8)
        xOxList[1] = 'X'
        isFull[1] = True
        counter += 1
    if pos_x <= 190 and (380 < pos_y < 570 and not isFull[2]):
        pygame.draw.line(screen, WHITE, (35, 435), (160, 560), 8)
        pygame.draw.line(screen, WHITE, (160, 435), (35, 560), 8)
        xOxList[2] = 'X'
        isFull[2] = True
        counter += 1
    # # İkinci sütun
    if (190 < pos_x <= 380) and pos_y <= 190 and not isFull[3]:
        pygame.draw.line(screen, WHITE, (240, 35), (365, 160), 8)
        pygame.draw.line(screen, WHITE, (365, 35), (240, 160), 8)
        xOxList[3] = 'X'
        isFull[3] = True
        counter += 1
    if (190 < pos_x <= 380) and (190 < pos_y < 380) and not isFull[4]:
        pygame.draw.line(screen, WHITE, (240, 240), (365, 365), 8)
        pygame.draw.line(screen, WHITE, (365, 240), (240, 365), 8)
        xOxList[4] = 'X'
        isFull[4] = True
        counter += 1
    if (190 < pos_x <= 380) and (380 < pos_y < 570) and not isFull[5]:
        pygame.draw.line(screen, WHITE, (240, 435), (365, 560), 8)
        pygame.draw.line(screen, WHITE, (365, 435), (240, 560), 8)
        xOxList[5] = 'X'
        isFull[5] = True
        counter += 1
    # Üçüncü sütun
    if (380 < pos_x <= 570) and pos_y <= 190 and not isFull[6]:
        pygame.draw.line(screen, WHITE, (435, 35), (560, 160), 8)
        pygame.draw.line(screen, WHITE, (560, 35), (435, 160), 8)
        xOxList[6] = 'X'
        isFull[6] = True
        counter += 1
    if (380 < pos_x <= 570) and (190 < pos_y < 380) and not isFull[7]:
        pygame.draw.line(screen, WHITE, (435, 240), (560, 365), 8)
        pygame.draw.line(screen, WHITE, (560, 240), (435, 365), 8)
        xOxList[7] = 'X'
        isFull[7] = True
        counter += 1
    if (380 < pos_x <= 570) and (380 < pos_y < 570) and not isFull[8]:
        pygame.draw.line(screen, WHITE, (435, 435), (560, 560), 8)
        pygame.draw.line(screen, WHITE, (560, 435), (435, 560), 8)
        xOxList[8] = 'X'
        isFull[8] = True
        counter += 1


def player2(pos_x, pos_y):
    # Birinci sütun
    global counter
    if pos_x <= 190 and pos_y <= 190 and not isFull[0]:
        pygame.draw.circle(screen, BLACK, (100, 100), 70, 5)
        xOxList[0] = 'O'
        isFull[0] = True
        counter += 1
    if pos_x <= 190 and (190 < pos_y < 380) and not isFull[1]:
        pygame.draw.circle(screen, BLACK, (100, 300), 70, 5)
        xOxList[1] = 'O'
        isFull[1] = True
        counter += 1
    if pos_x <= 190 and (380 < pos_y < 570) and not isFull[2]:
        pygame.draw.circle(screen, BLACK, (100, 500), 70, 5)
        xOxList[2] = 'O'
        isFull[2] = True
        counter += 1
    # İkinci sütun
    if (190 < pos_x <= 380) and pos_y <= 190 and not isFull[3]:
        pygame.draw.circle(screen, BLACK, (300, 100), 70, 5)
        xOxList[3] = 'O'
        isFull[3] = True
        counter += 1
    if (190 < pos_x <= 380) and (190 < pos_y < 380) and not isFull[4]:
        pygame.draw.circle(screen, BLACK, (300, 300), 70, 5)
        xOxList[4] = 'O'
        isFull[4] = True
        counter += 1
    if (190 < pos_x <= 380) and (380 < pos_y < 570) and not isFull[5]:
        pygame.draw.circle(screen, BLACK, (300, 500), 70, 5)
        xOxList[5] = 'O'
        isFull[5] = True
        counter += 1
    # Üçüncü sütun
    if (380 < pos_x <= 570) and pos_y <= 190 and not isFull[6]:
        pygame.draw.circle(screen, BLACK, (500, 100), 70, 5)
        xOxList[6] = 'O'
        isFull[6] = True
        counter += 1
    if (380 < pos_x <= 570) and (190 < pos_y < 380) and not isFull[7]:
        pygame.draw.circle(screen, BLACK, (500, 300), 70, 5)
        xOxList[7] = 'O'
        isFull[7] = True
        counter += 1
    if (380 < pos_x <= 570) and (380 < pos_y < 570) and not isFull[8]:
        pygame.draw.circle(screen, BLACK, (500, 500), 70, 5)
        xOxList[8] = 'O'
        isFull[8] = True
        counter += 1


def win_condition():
    if counter % 2 == 1:
        winner = 'X'
    else:
        winner = 'O'
    # sütun
    if xOxList[0] == xOxList[1] == xOxList[2]:
        print(winner + ' kazandı')
    if xOxList[3] == xOxList[4] == xOxList[5]:
        print(winner + ' kazandı')
    if xOxList[6] == xOxList[7] == xOxList[8]:
        print(winner + ' kazandı')

    # satır
    if xOxList[0] == xOxList[3] == xOxList[6]:
        print(winner + ' kazandı')
    if xOxList[1] == xOxList[4] == xOxList[7]:
        print(winner + ' kazandı')
    if xOxList[2] == xOxList[5] == xOxList[8]:
        print(winner + ' kazandı')

    # diagonal
    if xOxList[0] == xOxList[4] == xOxList[8]:
        print(winner + ' kazandı')
    if xOxList[2] == xOxList[4] == xOxList[6]:
        print(winner + ' kazandı')


counter = 0


def game(pos_x, pos_y):
    global counter
    if counter % 2 == 0:
        player1(pos_x, pos_y)
    else:
        player2(pos_x, pos_y)
    win_condition()


drawing_lines()
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            game(pos[0], pos[1])
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
