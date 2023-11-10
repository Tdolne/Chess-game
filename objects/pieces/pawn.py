from objects.board.tile import Tile

import pygame

class Pawn:
    '''
    Class representing a single pawn piece.

    Attributes:
        surface: The pygame.surface object representing the pawn's
                 position
        rect: The pygame.rect object that gets drawn to the screen
    '''
    surface: pygame.Surface
    rect: pygame.Rect
    color: str
    tile: Tile
    image: pygame.Surface

    def __init__(self, color: str, pawn_number: int, tiles: list) -> None:
        self.pawn_number = pawn_number
        self.color = color

        self.tile = self.get_correct_tile(tiles)
        self.image = self.load_image(color)
        self.position = self.tile.center_position
        self.surface = pygame.Surface((self.tile.size, self.tile.size))
        self.rect = self.surface.get_rect(center=self.position)

    def get_correct_tile(self, tiles: list) -> Tile:
        for tile in tiles:
            if (tile.position_indices == (self.pawn_number, 6)
                and self.color == 'white'):
                return tile
            elif (tile.position_indices == (self.pawn_number, 1)
                and self.color == 'black'):
                return tile

        raise ValueError(
            f'Could not find the correct tile for pawn {self.pawn_number} and color {self.color}'
            )

    def load_image(self, color: str) -> pygame.Surface:
        if color == 'white':
            return pygame.image.load('sprites/white_pawn.png')
        elif color == 'black':
            return pygame.image.load('sprites/black_pawn.png')
        else:
            raise ValueError(
                f'Color {color} is not valid and should be either white or black'
                )

    def update_position_from_resize(self, new_tiles: list[Tile]) -> None:
        old_size = self.tile.size
        self.tile = self.get_correct_tile(new_tiles)

        self.position = self.tile.center_position
        self.surface = pygame.Surface((self.tile.size, self.tile.size))
        self.image = pygame.transform.scale_by(self.image, self.tile.size/old_size)
        self.rect = self.surface.get_rect(center=self.position)


def create_all_pawns(tile_list: list) -> tuple[list, list]:
    white_pawns = []
    black_pawns = []
    for pawn_number in range(8):
        white_pawns.append(Pawn('white', pawn_number, tile_list))
        black_pawns.append(Pawn('black', pawn_number, tile_list))

    return white_pawns, black_pawns