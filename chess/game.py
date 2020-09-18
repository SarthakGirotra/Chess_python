import pygame
from .board import Board
from .constants import WHITE, BLACK, BLUE, SQUARE_SIZE


class Game:
    def __init__(self, win):
        self.win = win
        self._init()

    def _init(self):
        self.board = Board(self.win)
        self.turn = WHITE
        self.valid_moves = []
        self.selected = None

    def update(self):
        self.board.draw_board()
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def select(self, row, col):

        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                #self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            king, P = self.board.check_Check()
            if king:
                self.valid_moves = self.board.valid_moves_check(P, king, piece)
            else:
                self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)

        if self.selected and (row, col) in self.valid_moves:
            if piece != 0:
                self.board.remove(row, col)
            self.board.move(self.selected, row, col)

            self.change_turn()

        else:
            return False
        return True

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

    def undo(self):
        print('undo')

    def reset(self):
        self._init()
        print('Game Reset')
