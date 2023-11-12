import pygame
from objects.board.tile import Tile

class King:
    '''
    Class representing a single pawn piece.

    Attributes:
        surface: The pygame.surface object representing the pawn's
                 position
        rect: The pygame.rect object that gets drawn to the screen
        color: The color of the pawn, either 'white' or 'black'
        tile: The tile object that the pawn is currently on
        image: The pygame.surface object containing the pawn's image
    '''
    surface: pygame.Surface
    rect: pygame.Rect
    color: str
    tile: Tile
    image: pygame.Surface

    def __init__(self, color: str, tiles: list) -> None:
        self.color = color

        self.tile = self.get_initial_tile(tiles)
        self.image = self.load_image(color)
        self.position = self.tile.center_position
        self.surface = pygame.Surface((self.tile.size, self.tile.size))
        self.rect = self.surface.get_rect(center=self.position)

    def get_initial_tile(self, tiles: list) -> Tile:
        for tile in tiles:
            if (tile.position_indices == (4, 7)
                and self.color == 'white'):
                return tile
            elif (tile.position_indices == (3, 0)
                and self.color == 'black'):
                return tile

        raise ValueError(
            f'Could not find the correct tile for the {self.color} king')

    def load_image(self, color: str) -> pygame.Surface:
        if color == 'white':
            return pygame.image.load('sprites/white_king.png')
        elif color == 'black':
            return pygame.image.load('sprites/black_king.png')
        else:
            raise ValueError(
                f'Color {color} is not valid and should be either white or black'
                )

    def update_position_from_resize(self, new_tiles: list[Tile]) -> None:
        old_size = self.tile.size
        self.tile = self.get_initial_tile(new_tiles)

        self.position = self.tile.center_position
        self.surface = pygame.Surface((self.tile.size, self.tile.size))
        self.image = pygame.transform.scale_by(self.image, self.tile.size/old_size)
        self.rect = self.surface.get_rect(center=self.position)

def create_kings(tiles: list[Tile]):
    white_king = King('white', tiles)
    black_king = King('black', tiles)

    return white_king, black_king