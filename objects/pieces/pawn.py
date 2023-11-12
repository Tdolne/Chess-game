from objects.board.tile import Tile

import pygame

class Pawn:
    '''
    Class representing a single pawn piece.

    Attributes:
        pawn_number: The number of the pawn, from 0 to 7, indicating it's
                     horizontal position on the board
        surface: The pygame.surface object representing the pawn's
                 position
        rect: The pygame.rect object that gets drawn to the screen
        color: The color of the pawn, either 'white' or 'black'
        tile: The tile object that the pawn is currently on
        image: The pygame.surface object containing the pawn's image
    '''
    pawn_number: int
    surface: pygame.Surface
    rect: pygame.Rect
    color: str
    tile: Tile
    image: pygame.Surface

    def __init__(self, color: str, pawn_number: int, tiles: list) -> None:
        self.pawn_number = pawn_number
        self.color = color

        self.tile = self.get_initial_tile(tiles)
        self.image = self.load_image(color)
        self.position = self.tile.center_position
        self.surface = pygame.Surface((self.tile.size, self.tile.size))
        self.rect = self.surface.get_rect(center=self.position)

    def get_initial_tile(self, tiles: list) -> Tile:
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