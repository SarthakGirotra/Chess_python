import pygame
from .board import Board
from .constants import WHITE, BLACK, BLUE, SQUARE_SIZE


class Game:
    def __init__(self, win):
        self.win = win
        self.board = Board(self.win)
        self.turn = WHITE
        self.valid_moves = []
        self.selected = None

    def update(self):
        self.board.draw_board()
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def select(self, row, col):
        # if self.selected:
        #     result= se
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False

    def change_turn(self):
        self.valid_moves = []
        if self.turn == WHITE:
            self.turn = BLACK
        else:
            self.turn = WHITE

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE +
                                                SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 12)
