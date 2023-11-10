import pygame

from config import Config


class Tile:
    """
    Class representing a single tile on the chess board.

    Attributes:
        size:             The size of the tile, represented by an integer
        position_indices: The position indices of the tile, as a tuple
                          of two integers
        center_position:  The center position of the tile,
                          as a tuple of two coordinates
        color:            The color of the tile, represented by a tuple of three
                          integers indicating the RGB values.
        surface:          The Surface object representing the pawn's position
        rect:             The Rect object that gets drawn to the screen

    """

    size: int
    position_indices: tuple[int, int]
    center_position: tuple[float, float]
    color: tuple
    surface: pygame.Surface
    rect: pygame.Rect

    def __init__(self, tile_size: int, position_indices: tuple[int, int]) -> None:
        self.size = tile_size
        self.position_indices = position_indices
        self.center_position = self.find_center_position()
        self.color = self.determine_color()
        self.surface = pygame.Surface((tile_size, tile_size))
        self.surface.fill(self.color)
        self.rect = self.surface.get_rect(center=self.center_position)

    def find_center_position(self) -> tuple[float, float]:
        return (
            self.position_indices[0] * self.size + self.size // 2,
            self.position_indices[1] * self.size + self.size // 2,
        )

    def determine_color(self) -> tuple[int, int, int]:
        if (self.position_indices[0] + self.position_indices[1]) % 2 == 0:
            # If the sum of the indices is even, the tile should be white
            return Config.white_color
        else:
            return Config.black_color

    def update_tile_size(self, new_size: int) -> None:
        self.size = new_size
        self.center_position = self.find_center_position()
        self.surface = pygame.Surface((self.size, self.size))
        self.surface.fill(self.color)
        self.rect = self.surface.get_rect(center=self.center_position)
