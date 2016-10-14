ALPHA = 'abcdefgh'

class Cell(object):
    def __init__(self, position):
        # position - tuple
        # ('b', 2)
        # ('c', 4)
        self.position = position
        self.available = True
        self.has_figure = None

    def occupy(self, figure):
        self.has_figure = figure
        self.avail = False

    def free(self):
        self.has_figure = None
        self.avail = True


class Board(object):
    def __init__(self, board):
        self.board = board
    
    @staticmethod
    def get_board(size):
        # size - tuple
        # (4, 4)
        # (2, 2)
        board = [[Cell((ALPHA[i], j+1))
                          for j in range(size[1])]
                          for i in range(size[0])]
        return Board(board)

    def setup_fig(self, fig, cell):
        # fig - Figure
        # cell - tuple
        # ('a', 2)
        c = self.board[ALPHA.index(cell[0])][cell[1]-1]
        c.occupy(fig)

    def remove_fig(self, fig, cell):
        c = self.board[ALPHA.index(cell[0])][cell[1]-1]
        c.free()

    def show_board(self):
        self.sh_board = list(zip(*self.board))
        for column in reversed(self.sh_board):
            print('\n')
            for cell in column:
                sym = cell.has_figure.name if cell.has_figure else '.'
                print(sym, end='')

    def __repr__(self):        
        return 'Board({}x{})'.format(len(self.board),
                                     len(self.board[0]))
