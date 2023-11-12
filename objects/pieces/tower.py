import pygame

from objects.board.tile import Tile

class Tower:
    '''
    Class representing a single tower piece

    Attributes:
        start_position: String indicating the starting position of the
                        tower, either 'left' or 'right'
        surface: The pygame.surface object representing the tower's
                 position
        rect: The pygame.rect object that gets drawn to the screen
        color: The color of the tower, either 'white' or 'black'
        tile: The tile object that the tower is currently on
        image: The pygame.surface object containing the tower's image
    '''
    start_position: str
    surface: pygame.Surface
    rect: pygame.Rect
    color: str
    tile: Tile
    image: pygame.Surface

    def __init__(self, color: str, tiles: list, start_position: str) -> None:
        self.color = color
        self.start_position = start_position

        self.tile = self.get_initial_tile(tiles)
        self.image = self.load_image(color)
        self.position = self.tile.center_position
        self.surface = pygame.Surface((self.tile.size, self.tile.size))
        self.rect = self.surface.get_rect(center=self.position)

    def get_initial_tile(self, tiles: list) -> Tile:
        horizontal_position = 0 if self.start_position == 'left' else 7
        for tile in tiles:
            if (tile.position_indices == (horizontal_position, 7)
                and self.color == 'white'):
                return tile
            elif (tile.position_indices == (horizontal_position, 0)
                and self.color == 'black'):
                return tile

        raise ValueError(
            f'Could not find the correct tile for the {self.color} king')

    def load_image(self, color: str) -> pygame.Surface:
        if color == 'white':
            return pygame.image.load('sprites/white_tower.png')
        elif color == 'black':
            return pygame.image.load('sprites/black_tower.png')
        else:
            raise ValueError(
                f'Color {color} is not valid and should be either white or black'
                )