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

    def __init__(self):
        self.surface = pygame.Surface((30, 30))
        self.surface.fill((255, 0, 0))
        self.rect = self.surface.get_rect(center=(250, 250))
