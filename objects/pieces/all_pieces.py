import pygame

from objects.pieces.pawn import Pawn
from objects.pieces.horse import Horse
from objects.pieces.kings import King
from objects.board.tile import Tile

class AllPieces:
    pawns: list[Pawn]
    horses: list[Horse]
    kings: list[King]
    all_pieces: list

    def __init__(self, tiles: list) -> None:
        self.pawns = self.create_all_pawns(tiles)
        self.horses = self.create_horses(tiles)
        self.kings = self.create_kings(tiles)

        self.all_pieces = self.pawns + self.horses + self.kings

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
    def create_horses(tiles: list[Tile]) -> list[Horse]:
        white_horses = [Horse('white', tiles, 'left'),
                        Horse('white', tiles, 'right')]
        black_horses = [Horse('black', tiles, 'left'),
                        Horse('black', tiles, 'right')]

        return white_horses + black_horses