import pygame
from chess.constants import WIDTH, HEIGHT, SQUARE_SIZE, FPS
from chess.board import Board
from chess.game import Game
from chess.piece import Piece
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Chess')
# blit is x,y col,row
# y is 75 *n.2  where n is row
# 520 for 8th row
# x is 75* (n-1).93
# if x=0 row =-5


def get_pos(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():

    game = Game(WIN)
    p = game.board.get_piece(6, 1)
    game.board.move(p, 2, 4)
    game.update()
    # print(game.board.board)
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
    pygame.quit()


main()
