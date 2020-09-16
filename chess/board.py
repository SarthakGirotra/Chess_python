from .piece import Piece
import pygame
from .constants import SQUARE_SIZE, BROWN, CREAM, COLS, ROWS, BLACK, WHITE, MOVES, BP, WP, BR, WR, BH, WH, BB, WB, BQ, WQ, BK, WK


class Board:
    def __init__(self, win):
        self.win = win

        self.board = []
        self.create_board()
        self.draw_board()

    def draw_squares(self, win):
        win.fill(BROWN)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, CREAM, (row*SQUARE_SIZE,
                                              col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                # pawn
                if row == 1 or row == 6:
                    type = "pawn"
                    if row == 1:
                        color = BLACK
                    else:
                        color = WHITE
                    self.board[row].append(Piece(row, col, color, type))
                elif row == 0:
                    color = BLACK
                    self._elif(row, col, color)
                elif row == 7:
                    color = WHITE
                    self._elif(row, col, color)
                else:
                    self.board[row].append(0)

    def _elif(self, row, col, color):
        if col == 7 or col == 0:
            type = "rook"
        elif col == 1 or col == 6:
            type = "horse"
        elif col == 2 or col == 5:
            type = "bishop"
        elif col == 3:
            type = "queen"
        elif col == 4:
            type = "king"
        self.board[row].append(
            Piece(row, col, color, type))

    def piece_elif(self, piece):

        if piece.type == "pawn":
            if piece.color == WHITE:
                self.win.blit(WP, (piece.x, piece.y))
            else:
                self.win.blit(BP, (piece.x, piece.y))
        elif piece.type == "rook":
            if piece.color == WHITE:
                self.win.blit(WR, (piece.x, piece.y))
            else:
                self.win.blit(BR, (piece.x, piece.y))
        elif piece.type == "horse":
            if piece.color == WHITE:
                self.win.blit(WH, (piece.x, piece.y))
            else:
                self.win.blit(BH, (piece.x, piece.y))
        elif piece.type == "bishop":
            if piece.color == WHITE:
                self.win.blit(WB, (piece.x, piece.y))
            else:
                self.win.blit(BB, (piece.x, piece.y))
        elif piece.type == "queen":
            if piece.color == WHITE:
                self.win.blit(WQ, (piece.x, piece.y))
            else:
                self.win.blit(BQ, (piece.x, piece.y))
        else:
            if piece.color == WHITE:
                self.win.blit(WK, (piece.x, piece.y))
            else:
                self.win.blit(BK, (piece.x, piece.y))

    def draw_board(self):
        self.draw_squares(self.win)
        for row in range(ROWS):
            for col in range(COLS):
                P = self.board[row][col]
                if P:
                    self.piece_elif(P)
        pygame.display.update()

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        if piece.type == "pawn":
            if row == ROWS-1 or row == 0:
                piece.make_queen()
        piece.move(row, col)

    def get_piece(self, row, col):
        return self.board[row][col]

    def get_valid_moves(self, piece):
        moves = {}
        if piece.type == "rook" or piece.type == "bishop" or piece.type == "queen":
            moves = self.get_valid_moves_cont(piece)

        else:
            pass
        return moves

    def get_valid_moves_cont(self, piece):
        # piece = {color: string, type:string, row: int, col: int}
        # self = {board: [[piece | 0]]}
        board_status = {}
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col]:
                    board_status[(row, col)] = self.board[row][col].color

        valid_moves = {}
        for move in MOVES[piece.type]:
            for i in range(1, 9):
                current_pos = (i*move[0] + piece.row,
                               i*move[1] + piece.col)
                if (current_pos[0] < 0 or current_pos[0] > 7 or current_pos[1] < 0 or current_pos[1] > 7):
                    continue

                board_piece = board_status.get(current_pos, False)
                if (not board_piece):
                    valid_moves[current_pos] = []
                    continue

                else:
                    if (board_piece != piece.color):
                        valid_moves[current_pos] = []
                    break

        return valid_moves
