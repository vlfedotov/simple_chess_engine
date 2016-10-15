from board import Board
from figures import Queen, Rook, Bishop, Knight
from opponents import Whites, Blacks
from position import Position


if __name__ == '__main__':
    board = Board.get_board((8, 8))
    q = Queen(board, ('b', 7))
    r = Rook(board, ('g', 3))
    whites = Whites()
    blacks = Blacks()
    whites.add_figure(q)
    blacks.add_figure(r)
    # board.show_board()
    pos1 = Position(board, whites, blacks)

    b = Bishop(board, ('e', 1))
    whites.add_figure(b)
    r = Rook(board, ('h', 5))
    blacks.add_figure(r)
    pos2 = Position(board, whites, blacks)

    board1, whites1, blacks1 = pos1.get_position()
    board1.show_board()
    board.show_board()

    print(len(whites.avail_moves))
    print(len(whites1.avail_moves))