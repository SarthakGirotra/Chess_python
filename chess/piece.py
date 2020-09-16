import pygame
from .constants import SQUARE_SIZE


class Piece:
    def __init__(self, row, col, color, type):
        self.row = row
        self.col = col
        self.color = color
        self.type = type
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        if self.col > 0:
            self.x = SQUARE_SIZE*((self.col-1)+0.97)
        else:
            self.x = -5
        self.y = SQUARE_SIZE*(self.row+0.2)

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def make_queen(self):
        self.type = "queen"

    def __repr__(self):
        return str(self.type)
