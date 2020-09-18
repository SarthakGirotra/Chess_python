import pygame
from chess.constants import WIDTH, HEIGHT, SQUARE_SIZE, FPS
from chess.board import Board
from chess.game import Game
from chess.piece import Piece
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Chess')


def get_pos(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():

    game = Game(WIN)
    game.update()

    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_pos(pos)

                game.select(row, col)
                game.update()
            # if event.type == pygame.KEYDOWN:
            #     game.reset()

        
    pygame.quit()


main()
