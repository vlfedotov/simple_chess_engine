from .board import ALPHA


class Figure(object):
    def __init__(self, side, cell, name):
        self.cell = cell
        self.name = name
        self.side = side
        # self.board = self.side.board
        self.board_table = self.side.board.board
        self.avail_moves = set()  # self.get_avail_moves() - {self.cell}
        self.is_under_attack = False
        self.side.add_figure(self)

    def get_avail_moves(self, target_cell=None):
        pass

    # def move(self, to_cell):
    #     self.board.remove_fig(self.cell)
    #     self.cell = to_cell
    #     self.board.setup_fig(self, self.cell)
    #     # self.avail_moves = self.get_avail_moves()

    def check_move(self, target_cell):
        if target_cell in self.side.opponent.occupation:
            return target_cell, False
        elif target_cell in self.side.occupation:
            return None, False
        elif target_cell[1] < 1 or target_cell[1] > len(self.board_table):
            return None, False
        else:
            return target_cell, True

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
        DOWN = UP = LEFT = RIGHT = True
        avail_moves = set()
        for i in range(1, len(self.board_table)):
            if UP:
                try:
                    move = (cell[0], cell[1]+i)
                    res_move, cont = self.check_move(move)
                    if res_move:
                        avail_moves.add(res_move)
                    if not cont:
                        UP = False
                except IndexError:
                    UP = False
            if DOWN:
                try:
                    move = (cell[0], cell[1]-i)
                    # if move[1] <
                    res_move, cont = self.check_move(move)
                    if res_move:
                        avail_moves.add(res_move)
                    if not cont:
                        DOWN = False
                except:
                    DOWN = False
            if LEFT:
                try:
                    move = (ALPHA[ALPHA.index(cell[0])-i], cell[1])
                    res_move, cont = self.check_move(move)
                    if res_move:
                        avail_moves.add(res_move)
                    if not cont:
                        LEFT = False
                except:
                    LEFT = False
            if RIGHT:
                try:
                    move = (ALPHA[ALPHA.index(cell[0])+i], cell[1])
                    res_move, cont = self.check_move(move)
                    if res_move:
                        avail_moves.add(res_move)
                    if not cont:
                        RIGHT = False
                except:
                    RIGHT = False

        return avail_moves


class Bishop(Figure):
    def __init__(self, *args):
        super().__init__(*args, name='B')

    def get_avail_moves(self, target_cell=None):
        cell = target_cell or self.cell
        LU = RU = LD = RD = True
        avail_moves = set()
        for i in range(1, len(self.board_table)):
            if LU:
                try:
                    move = (ALPHA[ALPHA.index(cell[0])-i], cell[1]+i)
                    if ALPHA.index(cell[0])-i < 0:
                        LU = False
                    else:
                        res_move, cont = self.check_move(move)
                        if res_move:
                            avail_moves.add(res_move)
                        if not cont:
                            LU = False
                except IndexError:
                    LU = False
            if RU:
                try:
                    move = (ALPHA[ALPHA.index(cell[0])+i], cell[1]+i)
                    # print('ru', move)
                    res_move, cont = self.check_move(move)
                    if res_move:
                        avail_moves.add(res_move)
                    if not cont:
                        RU = False
                except IndexError:
                    RU = False
            if LD:
                try:
                    move = (ALPHA[ALPHA.index(cell[0])-i], cell[1]-i)
                    if ALPHA.index(cell[0])-i < 0:
                        LD = False
                    else:
                        res_move, cont = self.check_move(move)
                        if res_move:
                            avail_moves.add(res_move)
                        if not cont:
                            LD = False
                except IndexError:
                    LD = False
            if RD:
                try:
                    move = (ALPHA[ALPHA.index(cell[0])+i], cell[1]-i)
                    # print('rd', move)
                    res_move, cont = self.check_move(move)
                    if res_move:
                        avail_moves.add(res_move)
                    if not cont:
                        RD = False
                except IndexError:
                    RD = False

        return avail_moves
        

class Knight(Figure):
    def __init__(self, *args):
        super().__init__(*args, name='K')

    def get_avail_moves(self, target_cell=None):
        cell = target_cell or self.cell
        avail_moves = set()

        for i in [-2, -1, 1, 2]:
            for j in [-(3-abs(i)), 3-abs(i)]:
                try:
                    move = (ALPHA[ALPHA.index(cell[0]) + i], cell[1] + j)
                    if ALPHA.index(cell[0]) + i < 0:
                        pass
                    else:
                        res_move, _ = self.check_move(move)
                        if res_move:
                            avail_moves.add(res_move)
                except IndexError:
                    pass
        return avail_moves
