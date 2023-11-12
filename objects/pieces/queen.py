import pygame

from objects.board.tile import Tile

class Queen:
    '''
    Class representing a single queen piece.

    Attributes:
        surface: The pygame.surface object representing the queen's
                 position
        rect: The pygame.rect object that gets drawn to the screen
        color: The color of the queen, either 'white' or 'black'
        tile: The tile object that the queen is currently on
        image: The pygame.surface object containing the queen's image
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
            if (tile.position_indices == (3, 7)
                and self.color == 'white'):
                return tile
            elif (tile.position_indices == (3, 0)
                and self.color == 'black'):
                return tile

        raise ValueError(
            f'Could not find the correct tile for the {self.color} king')

    def load_image(self, color: str) -> pygame.Surface:
        if color == 'white':
            return pygame.image.load('sprites/white_queen.png')
        elif color == 'black':
            return pygame.image.load('sprites/black_queen.png')
        else:
            raise ValueError(
                f'Color {color} is not valid and should be either white or black'
                )
