import pygame

from objects.pieces.pawn import Pawn
from objects.pieces.knight import Knight
from objects.pieces.bishop import Bishop
from objects.pieces.king import King
from objects.pieces.tower import Tower
from objects.pieces.queen import Queen
from objects.board.tile import Tile

class AllPieces:
    pawns: list[Pawn]
    knights: list[Knight]
    bishops: list[Bishop]
    kings: list[King]
    queens: list[Queen]
    towers: list[Tower]
    all_pieces: list

    def __init__(self, tiles: list) -> None:
        self.pawns = self.create_all_pawns(tiles)
        self.knights = self.create_knights(tiles)
        self.bishops = self.create_bishops(tiles)
        self.kings = self.create_kings(tiles)
        self.queens = self.create_queens(tiles)
        self.towers = self.create_towers(tiles)

        self.all_pieces = (self.pawns
                           + self.knights
                           + self.bishops
                           + self.kings
                           + self.queens
                           + self.towers)

    def update_board_size(self, new_tiles: list[Tile]) -> None:
        for piece in self.all_pieces:

            old_size = piece.tile.size
            piece.tile = piece.get_initial_tile(new_tiles)

            piece.position = piece.tile.center_position
            piece.surface = pygame.Surface((piece.tile.size, piece.tile.size))
            piece.image = pygame.transform.scale_by(piece.image, piece.tile.size/old_size)
            piece.rect = piece.surface.get_rect(center=piece.position)

    @staticmethod
    def create_all_pawns(tile_list: list[Tile]) -> list[Pawn]:
        white_pawns = []
        black_pawns = []
        for pawn_number in range(8):
            white_pawns.append(Pawn('white', pawn_number, tile_list))
            black_pawns.append(Pawn('black', pawn_number, tile_list))

        return white_pawns + black_pawns

    @staticmethod
    def create_kings(tiles: list[Tile]) -> list[King]:
        white_king = King('white', tiles)
        black_king = King('black', tiles)

        return [white_king, black_king]

    @staticmethod
    def create_queens(tiles: list[Tile]) -> list[Queen]:
        white_queen = Queen('white', tiles)
        black_queen = Queen('black', tiles)

        return [white_queen, black_queen]

    @staticmethod
    def create_knights(tiles: list[Tile]) -> list[Knight]:
        white_knights = [Knight('white', tiles, 'left'),
                        Knight('white', tiles, 'right')]
        black_knights = [Knight('black', tiles, 'left'),
                        Knight('black', tiles, 'right')]

        return white_knights + black_knights

    @staticmethod
    def create_bishops(tiles: list[Tile]) -> list[Bishop]:
        white_bishops = [Bishop('white', tiles, 'left'),
                         Bishop('white', tiles, 'right')]
        black_bishops = [Bishop('black', tiles, 'left'),
                         Bishop('black', tiles, 'right')]

        return white_bishops + black_bishops

    @staticmethod
    def create_towers(tiles: list[Tile]) -> list[Tower]:
        white_towers = [Tower('white', tiles, 'left'),
                        Tower('white', tiles, 'right')]
        black_towers = [Tower('black', tiles, 'left'),
                        Tower('black', tiles, 'right')]

        return white_towers + black_towers