from board import ALPHA
from opponents import Opponent


class Figure(Opponent):
    def __init__(self, board, cell, name):
        self.cell = cell
        self.board = board
        self.board.setup_fig(self, cell)
        self._is_alive = True
        self._avail_moves = self.get_avail_moves()
        self.name = name
        # self.correct_fig_name(name)
        # TODO
        # self._remove_onecolor_cells()

    def move(self, to_cell):
        if to_cell.available:
            self.cell = to_cell

class Queen(Figure):
    def __init__(self, board, cell):
        super().__init__(board, cell, 'Q')
    
    def get_avail_moves(self):
        rook_like_moves = Rook.get_avail_moves(self)
        bishop_like_moves = Bishop.get_avail_moves(self)
        return rook_like_moves | bishop_like_moves

    
class Rook(Figure):
    def __init__(self, board, cell):
        super().__init__(board, cell, 'R')
        self.name = 'R'

    def get_avail_moves(self):
        row_moves = [c.position for c
            in self.board.board[ALPHA.index(self.cell[0])]]
        col_moves = [c[self.cell[1]-1].position for c
            in self.board.board]
        return set(row_moves + col_moves)


class Bishop(Figure):
    def __init__(self, board, cell):
        super().__init__(board, cell, 'B')
        self.name = 'B'
    
    def get_avail_moves(self):
        diag_moves = set()
        let_idx = ALPHA.index(self.cell[0])
        for i in range(-let_idx, len(self.board.board)-let_idx):
            try:
                c = self.board.board[let_idx+i][self.cell[1]-1+i]
                diag_moves.add(c.position)
            except Exception:
                pass
            try:
                if self.cell[1]-1-i < 0:
                    continue
                c = self.board.board[let_idx+i][self.cell[1]-1-i]
                diag_moves.add(c.position)
            except Exception:
                pass
        return diag_moves
        

class Knight(Figure):
    def __init__(self, board, cell):
        super().__init__(board, cell, 'K')
        self.name = 'K'
    
    def get_avail_moves(self):
        kn_moves = set()

        for i in [-2, -1, 1, 2]:
            for j in [-(3-abs(i)), 3-abs(i)]:
                try:
                    c = self.board.board[ALPHA.index(self.cell[0])+i][self.cell[1]-1+j]
                    kn_moves.add(c.position)
                except Exception:
                    pass
        return kn_moves
