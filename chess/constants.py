import pygame
BLACK = (255, 255, 255)
WHITE = (0, 0, 0)
BROWN = (160, 82, 45)
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS
CREAM = (255, 253, 208)
BLUE = (0, 100, 255)
FPS = 60
BP = pygame.transform.scale(pygame.image.load('assets/bp.png'), (80, 60))
WP = pygame.transform.scale(pygame.image.load('assets/wp.png'), (80, 60))
BR = pygame.transform.scale(pygame.image.load('assets/bR.png'), (80, 60))
WR = pygame.transform.scale(pygame.image.load('assets/wR.png'), (80, 60))
BH = pygame.transform.scale(pygame.image.load('assets/bH.png'), (80, 60))
WH = pygame.transform.scale(pygame.image.load('assets/wH.png'), (80, 60))
BB = pygame.transform.scale(pygame.image.load('assets/bB.png'), (80, 60))
WB = pygame.transform.scale(pygame.image.load('assets/wB.png'), (80, 60))
BQ = pygame.transform.scale(pygame.image.load('assets/bQ.png'), (80, 60))
WQ = pygame.transform.scale(pygame.image.load('assets/wQ.png'), (80, 60))
BK = pygame.transform.scale(pygame.image.load('assets/bK.png'), (80, 60))
WK = pygame.transform.scale(pygame.image.load('assets/wK.png'), (80, 60))

MOVES = {
    'rook': [(1, 0), (-1, 0), (0, 1), (0, -1)],
    'bishop': [(-1, -1), (-1, 1), (1, -1), (1, 1)],
    'queen': [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
}
