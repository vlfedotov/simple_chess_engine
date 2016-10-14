from board import Board
from figures import Queen, Rook, Bishop, Knight


if __name__ == '__main__':
    board = Board.get_board((8, 8))
    b = Bishop(board, ('b', 4))
    print(sorted(list(b._avail_moves)))


