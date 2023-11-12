import pygame
from pygame.locals import QUIT, VIDEORESIZE
from objects.board.board import Board
from objects.board.tile import Tile
from objects.pieces.pawn import Pawn, create_all_pawns
from objects.pieces.king import King, create_kings
from objects.pieces.horse import Horse, create_horses
from config import Config

BOARD_SIZE = Config.board_size
FPS = 60
clock = pygame.time.Clock()
pygame.init()


def create_all_pieces(tiles: list[Tile]) -> list:
    white_pawns, black_pawns = create_all_pawns(tiles)
    white_king, black_king = create_kings(tiles)
    white_horses, black_horses = create_horses(tiles)

    all_pieces = white_pawns + black_pawns + [white_king, black_king]
    all_pieces += white_horses + black_horses

    return all_pieces

def main():
    display_surface = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE),
                                              pygame.RESIZABLE)
    pygame.display.set_caption('Chess')

    board = Board(min(display_surface.get_size()))
    all_pieces = create_all_pieces(board.tiles)

    running = True
    while running:
        for tile in board.tiles:
            display_surface.blit(tile.surface, tile.rect)
        for event in pygame.event.get():
            if event.type == VIDEORESIZE:
                board.update_board_size(min(event.size))
                for tile in board.tiles:
                    tile.update_tile_size(board.tile_size)
                for piece in all_pieces:
                    piece.update_position_from_resize(board.tiles)

            if event.type == QUIT:
                pygame.quit()
                exit()

        for piece in all_pieces:
            display_surface.blit(piece.image, piece.rect)

        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    main()