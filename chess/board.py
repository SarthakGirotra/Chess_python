from .piece import Piece
import pygame
from .constants import SQUARE_SIZE, BROWN, CREAM, COLS, ROWS, BLACK, WHITE, MOVES, BP, WP, BR, WR, BH, WH, BB, WB, BQ, WQ, BK, WK


class Board:
    def __init__(self, win):
        self.win = win

        self.board = []
        self.create_board()
        self.draw_board()
        self.history = []
        self.white_king = (7, 4)
        self.black_king = (0, 4)

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
        if piece.type == "king":
            if piece.color == BLACK:
                self.black_king = (row, col)
            else:
                self.white_king = (row, col)

        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        if piece.type == "pawn":
            if row == ROWS-1 or row == 0:
                piece.make_queen()
        piece.move(row, col)

    def get_piece(self, row, col):
        return self.board[row][col]

    def get_valid_moves(self, piece):

        if piece.type == "pawn":
            moves = self.get_valid_moves_pawn(piece)
        else:
            moves = self.get_valid_moves_cont(piece)
        return moves

    def get_valid_moves_cont(self, piece):

        # piece = {color: string, type:string, row: int, col: int}
        # self = {board: [[piece | 0]]}

        board_status = {}
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col]:
                    board_status[(row, col)] = self.board[row][col].color

        valid_moves = []
        for move in MOVES[piece.type]:
            if piece.type == 'king' or piece.type == 'horse':
                current_pos = (move[0]+piece.row, move[1]+piece.col)
                if (current_pos[0] < 0 or current_pos[0] > 7 or current_pos[1] < 0 or current_pos[1] > 7):
                    continue

                board_piece = board_status.get(current_pos, False)
                if (not board_piece):
                    valid_moves.append(current_pos)
                    continue

                else:
                    if (board_piece != piece.color):
                        valid_moves.append(current_pos)

            else:
                for i in range(1, 9):
                    current_pos = (i*move[0] + piece.row,
                                   i*move[1] + piece.col)
                    if (current_pos[0] < 0 or current_pos[0] > 7 or current_pos[1] < 0 or current_pos[1] > 7):
                        continue

                    board_piece = board_status.get(current_pos, False)
                    if (not board_piece):
                        valid_moves.append(current_pos)
                        continue

                    else:
                        if (board_piece != piece.color):
                            valid_moves.append(current_pos)
                        break

        return valid_moves

    def get_valid_moves_pawn(self, piece):
        moves = []
        board_status = {}
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col]:
                    board_status[(row, col)] = self.board[row][col].color

        if piece.color == BLACK:
            direction = 1
            forward = (piece.row+direction, piece.col)
            forward_ = (piece.row+2*direction, piece.col)
            if (not board_status.get(forward, False) and not board_status.get(forward_, False)):
                if piece.row == 1:
                    moves.append((piece.row + 2*direction, piece.col))

        else:
            direction = -1
            forward = (piece.row+direction, piece.col)
            forward_ = (piece.row+2*direction, piece.col)
            if (not board_status.get(forward, False) and not board_status.get(forward_, False)):
                if piece.row == 6:
                    moves.append((piece.row + 2*direction, piece.col))

        diagonals = [(piece.row+direction, piece.col-1),
                     (piece.row+direction, piece.col+1)]
        board_piece = board_status.get(forward, False)
        if (not board_piece):
            moves.append(forward)
        for d in diagonals:
            board_piece = board_status.get(d, False)
            if (board_piece and board_piece != piece.color):
                moves.append(d)
        return moves

    def remove(self, row, col):
        p = self.get_piece(row, col)
        print(p.color, p, "taken")
        self.history.append(p)
        self.board[row][col] = 0

    def check_Check(self):
        for row in range(ROWS):
            for col in range(COLS):
                P = self.get_piece(row, col)
                if P and P.type != "king":
                    moves = self.get_valid_moves(P)

                    if P.color == WHITE:
                        if self.black_king in moves:

                            return self.black_king, P
                    else:
                        if self.white_king in moves:

                            return self.white_king, P
        return None, None

    def valid_moves_check(self, checker, king, piece):
        moves = []
        if piece.type != 'king':
            moves = self.interject_checker(checker, piece, king)
        else:
            moves = self.move_king_check(
                king, checker, self.cover(king, checker))
        return moves

    def interject_checker(self, checker, piece, king):
        loc = []
        cur_moves = self.get_valid_moves(piece)
        if (checker.row, checker.col) in cur_moves:
            loc.append((checker.row, checker.col))
        path = []
        if checker.type != "pawn" and checker.type != "horse":
            for move in MOVES[checker.type]:
                current_pos = []
                for i in range(1, 9):
                    current_pos.append((i*move[0] + checker.row,
                                        i*move[1] + checker.col))
                    if king in current_pos:
                        path = current_pos

            if path:
                for moves in cur_moves:
                    if moves in path:
                        loc.append(moves)
        return loc

    def move_king_check(self, king, checker, cover):
        moves = []
        king_piece = self.get_piece(king[0], king[1])
        for move in MOVES['king']:
            current_pos = (move[0]+king[0], move[1]+king[1])
            if current_pos == (checker.row, checker.col) and cover == False:
                moves.append(current_pos)
            else:
                continue
            if(self.check_valid_move_king(current_pos, king_piece)):
                moves.append(current_pos)
        return moves

    def cover(self, king, checker):

        king_piece = self.get_piece(king[0], king[1])
        for row in range(ROWS):
            for col in range(COLS):
                P = self.get_piece(row, col)

                if P and P.color != king_piece.color:
                    moves = self.get_valid_moves_same_color(P)

                    if (checker.row, checker.col) in moves:

                        return True

        return False

    def check_valid_move_king(self, move, king_piece):
        for row in range(ROWS):
            for col in range(COLS):
                P = self.get_piece(row, col)
                if P and P.color != king_piece.color:
                    if move in self.get_valid_moves(P):
                        return False
                elif P and P.color == king_piece.color:
                    if move == (P.row, P.col):
                        return False

        return True
# todo  [add check_protection while moving],[cover to diff color pieces when check]

    def get_valid_moves_same_color(self, piece):
        temp = piece
        if temp.color == WHITE:
            temp.color = BLACK
        else:
            temp.color = WHITE
        moves = self.get_valid_moves(temp)
        if temp.color == WHITE:
            temp.color = BLACK
        else:
            temp.color = WHITE
        return moves

    def checkmate(self, king):
        pass
