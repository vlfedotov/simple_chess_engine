from .board import ALPHA


class Figure(object):
    def __init__(self, opponent, cell, name):
        self.cell = cell
        self.name = name
        self.opponent = opponent
        self.board_table = self.opponent.board.board
        self.avail_moves = set()  # self.get_avail_moves() - {self.cell}
        self.is_under_attack = False
        opponent.add_figure(self)

    def move(self, to_cell):
        self.cell = to_cell
        self.avail_moves = self.get_avail_moves()

    def get_avail_moves(self, target_cell):
        pass

    def check_move(self, target_cell):
        return self.get_avail_moves(target_cell) - {self.cell}

    # def __set__(self, key, value):
    #     setattr(key, self.cell, value)
    #     self.avail_moves = self.get_avail_moves(value) - {self.cell}


class Queen(Figure):
    def __init__(self, *args):
        super().__init__(*args, name='Q')
    
    def get_avail_moves(self, target_cell=None):
        cell = target_cell or self.cell
        rook_like_moves = Rook.get_avail_moves(self, cell)
        bishop_like_moves = Bishop.get_avail_moves(self, cell)
        return rook_like_moves | bishop_like_moves

    
class Rook(Figure):
    def __init__(self, *args):
        super().__init__(*args, name='R')

    def get_avail_moves(self, target_cell=None):
        cell = target_cell or self.cell
        row_moves = [c.position for c
                        in self.board_table[ALPHA.index(cell[0])]]
        col_moves = [c[cell[1]-1].position for c
                        in self.board_table]
        return set(row_moves + col_moves)


class Bishop(Figure):
    def __init__(self, *args):
        super().__init__(*args, name='B')

    def get_avail_moves(self, target_cell=None):
        cell = target_cell or self.cell
        diag_moves = set()
        let_idx = ALPHA.index(cell[0])
        for i in range(-let_idx, len(self.board_table)-let_idx):
            try:
                if cell[1]-1+i >= 0:
                    c = self.board_table[let_idx+i][cell[1]-1+i]
                    diag_moves.add(c.position)
            except IndexError:
                pass
            try:
                if cell[1]-1-i < 0:
                    continue
                c = self.board_table[let_idx+i][cell[1]-1-i]
                diag_moves.add(c.position)
            except IndexError:
                pass
        return diag_moves
        

class Knight(Figure):
    def __init__(self, *args):
        super().__init__(*args, name='K')

    def get_avail_moves(self, target_cell=None):
        cell = target_cell or self.cell
        kn_moves = set()

        for i in [-2, -1, 1, 2]:
            for j in [-(3-abs(i)), 3-abs(i)]:
                try:
                    c = self.board_table[ALPHA.index(cell[0])+i][cell[1]-1+j]
                    kn_moves.add(c.position)
                except IndexError:
                    pass
        return kn_moves
