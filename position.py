from copy import deepcopy

class Position(object):

    def __init__(self, board, whites, blacks):
        self.board  = deepcopy(board)
        self.whites = deepcopy(whites)
        self.blacks = deepcopy(blacks)

    def get_position(self):
        return self.board, self.whites, self.blacks

    """
    def save_board(self, board):
        new_board = Board.get_board((len(board.board), len(board.board[0])))
        # TODO
        return new_board

    def save_whites(self):
        pass

    def save_blacks(self):
        pass
    """