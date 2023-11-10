from objects.board.tile import Tile


class Board:
    size: int
    tile_size: int
    tiles: list[Tile]

    def __init__(self, board_size: int):
        self.size = board_size
        self.tile_size = self.size // 8
        self.tiles = self.create_tiles()


    def create_tiles(self) -> list:
        tiles = []
        for horizontal_index in range(8):
            for vertical_index in range(8):
                tiles.append(Tile(self.tile_size, (horizontal_index, vertical_index)))
        return tiles

    def update_board_size(self, new_size: int) -> None:
        self.size = new_size
        self.tile_size = self.size // 8
        self.tiles = self.create_tiles()


