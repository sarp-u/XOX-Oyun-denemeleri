import pygame, sys

TEAL = (0, 128, 128)
LINE = (0, 100, 100)
WHITE = (240, 240, 240)
BLACK = (30, 30, 30)

xOxList = ['', '', '', '', '', '', '', '', '']

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('XOX')
screen.fill(TEAL)


def drawing_lines():
    pygame.draw.line(screen, LINE, (0, 200), (600, 200), 8)
    pygame.draw.line(screen, LINE, (0, 400), (600, 400), 8)
    pygame.draw.line(screen, LINE, (200, 0), (200, 600), 8)
    pygame.draw.line(screen, LINE, (400, 0), (400, 600), 8)


drawing_lines()


def player1(pos_x, pos_y):
    # Birinci sütun
    if pos_x <= 190 and pos_y <= 190:
        pygame.draw.line(screen, WHITE, (35, 35), (160, 160), 8)
        pygame.draw.line(screen, WHITE, (160, 35), (35, 160), 8)
        xOxList[0] = 'X'
    if pos_x <= 190 and (190 < pos_y < 380):
        pygame.draw.line(screen, WHITE, (35, 240), (160, 365), 8)
        pygame.draw.line(screen, WHITE, (160, 240), (35, 365), 8)
        xOxList[1] = 'X'
    if pos_x <= 190 and (380 < pos_y < 570):
        pygame.draw.line(screen, WHITE, (35, 435), (160, 560), 8)
        pygame.draw.line(screen, WHITE, (160, 435), (35, 560), 8)
        xOxList[2] = 'X'
    # # İkinci sütun
    if (190 < pos_x <= 380) and pos_y <= 190:
        pygame.draw.line(screen, WHITE, (240, 35), (365, 160), 8)
        pygame.draw.line(screen, WHITE, (365, 35), (240, 160), 8)
        xOxList[3] = 'X'
    if (190 < pos_x <= 380) and (190 < pos_y < 380):
        pygame.draw.line(screen, WHITE, (240, 240), (365, 365), 8)
        pygame.draw.line(screen, WHITE, (365, 240), (240, 365), 8)
        xOxList[4] = 'X'
    if (190 < pos_x <= 380) and (380 < pos_y < 570):
        pygame.draw.line(screen, WHITE, (240, 435), (365, 560), 8)
        pygame.draw.line(screen, WHITE, (365, 435), (240, 560), 8)
        xOxList[5] = 'X'
    # Üçüncü sütun
    if (380 < pos_x <= 570) and pos_y <= 190:
        pygame.draw.line(screen, WHITE, (435, 35), (560, 160), 8)
        pygame.draw.line(screen, WHITE, (560, 35), (435, 160), 8)
        xOxList[6] = 'X'
    if (380 < pos_x <= 570) and (190 < pos_y < 380):
        pygame.draw.line(screen, WHITE, (435, 240), (560, 365), 8)
        pygame.draw.line(screen, WHITE, (560, 240), (435, 365), 8)
        xOxList[7] = 'X'
    if (380 < pos_x <= 570) and (380 < pos_y < 570):
        pygame.draw.line(screen, WHITE, (435, 435), (560, 560), 8)
        pygame.draw.line(screen, WHITE, (560, 435), (435, 560), 8)
        xOxList[8] = 'X'


def player2(pos_x, pos_y):
    # Birinci sütun
    if pos_x <= 190 and pos_y <= 190:
        pygame.draw.circle(screen, BLACK, (100, 100), 70, 5)
        xOxList[0] = 'O'
    if pos_x <= 190 and (190 < pos_y < 380):
        pygame.draw.circle(screen, BLACK, (100, 300), 70, 5)
        xOxList[1] = 'O'
    if pos_x <= 190 and (380 < pos_y < 570):
        pygame.draw.circle(screen, BLACK, (100, 500), 70, 5)
        xOxList[2] = 'O'
    # İkinci sütun
    if (190 < pos_x <= 380) and pos_y <= 190:
        pygame.draw.circle(screen, BLACK, (300, 100), 70, 5)
        xOxList[3] = 'O'
    if (190 < pos_x <= 380) and (190 < pos_y < 380):
        pygame.draw.circle(screen, BLACK, (300, 300), 70, 5)
        xOxList[4] = 'O'
    if (190 < pos_x <= 380) and (380 < pos_y < 570):
        pygame.draw.circle(screen, BLACK, (300, 500), 70, 5)
        xOxList[5] = 'O'
    # Üçüncü sütun
    if (380 < pos_x <= 570) and pos_y <= 190:
        pygame.draw.circle(screen, BLACK, (500, 100), 70, 5)
        xOxList[6] = 'O'
    if (380 < pos_x <= 570) and (190 < pos_y < 380):
        pygame.draw.circle(screen, BLACK, (500, 300), 70, 5)
        xOxList[7] = 'O'
    if (380 < pos_x <= 570) and (380 < pos_y < 570):
        pygame.draw.circle(screen, BLACK, (500, 500), 70, 5)
        xOxList[8] = 'O'


def game(pos_x, pos_y):
    player1(pos_x,pos_y)


while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            game(pos[0], pos[1])
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
