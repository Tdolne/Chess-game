import pygame
from pygame.locals import QUIT
from objects.board.board import Board
from objects.board.tile import Tile
from config import Config

BOARD_SIZE = Config.board_size

def main():
    pygame.init()

    display_surface = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))
    pygame.display.set_caption('Chess')

    board = Board(BOARD_SIZE)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        for tile in board.tiles:
            display_surface.blit(tile.surface, tile.rect)


        pygame.display.update()

if __name__ == '__main__':
    main()