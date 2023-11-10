import pygame
from pygame.locals import QUIT, VIDEORESIZE
from objects.board.board import Board
from objects.board.tile import Tile
from objects.pieces.pawn import Pawn, create_all_pawns
from config import Config

BOARD_SIZE = Config.board_size
FPS = 60
clock = pygame.time.Clock()
pygame.init()

def main():
    display_surface = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE),
                                              pygame.RESIZABLE)
    pygame.display.set_caption('Chess')

    board = Board(min(display_surface.get_size()))
    white_pawns, black_pawns = create_all_pawns(board.tiles)
    all_pawns = white_pawns + black_pawns

    running = True
    while running:
        for tile in board.tiles:
            display_surface.blit(tile.surface, tile.rect)
        for event in pygame.event.get():
            if event.type == VIDEORESIZE:
                tiles = []
                board.update_board_size(min(event.size))
                for tile in board.tiles:
                    tile.update_tile_size(board.tile_size)
                    tiles.append(tile)
                for pawn in all_pawns:
                    pawn.update_position_from_resize(tiles)

            if event.type == QUIT:
                pygame.quit()
                exit()

        for pawn in all_pawns:
            display_surface.blit(pawn.image, pawn.rect)

        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    main()