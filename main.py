import pygame
from pygame.locals import QUIT, VIDEORESIZE
from objects.board.board import Board
from objects.board.tile import Tile
from objects.pieces.pawn import Pawn
from objects.pieces.kings import King
from objects.pieces.horse import Horse
from objects.pieces.all_pieces import AllPieces
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
    all_pieces = AllPieces(board.tiles)

    running = True
    while running:
        for tile in board.tiles:
            display_surface.blit(tile.surface, tile.rect)
        for event in pygame.event.get():
            if event.type == VIDEORESIZE:
                board.update_board_size(min(event.size))
                for tile in board.tiles:
                    tile.update_tile_size(board.tile_size)
                all_pieces.update_board_size(board.tiles)

            if event.type == QUIT:
                pygame.quit()
                exit()

        for piece in all_pieces.all_pieces:
            display_surface.blit(piece.image, piece.rect)

        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    main()