import pygame

from config import Config

class Tile:
    size: int
    center_position: tuple
    position_indices: tuple
    color: tuple

    def __init__(self, tile_size: int, position_indices: tuple) -> None:
        self.size = tile_size
        self.position_indices = position_indices
        self.center_position = self.find_center_position()
        self.color = self.determine_color()
        self.surface = pygame.Surface((tile_size, tile_size))
        self.surface.fill(self.color)
        self.rect = self.surface.get_rect(center=self.center_position)

    def find_center_position(self) -> tuple[float, float]:
        return (
            self.position_indices[0] * self.size+ self.size // 2,
            self.position_indices[1] * self.size+ self.size // 2)

    def determine_color(self) -> tuple[int, int, int]:
        if (self.position_indices[0]+self.position_indices[1]) % 2 == 0:
            # If the sum of the indices is even, the tile should be white
            return Config.white_color
        else:
            return Config.black_color
