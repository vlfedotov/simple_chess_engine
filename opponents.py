
class Opponent(object):
    def __init__(self):
        # self.correct_fig_name()
        self.occupation = []  # cells
        self.figures = []
        self.avail_moves = []

    def add_figure(self, figure):
        self.occupation += figure.cell.position
        self.correct_fig_name(figure)
        self.figures.append(figure)
        self.update_all_available_moves()

    def make_move(self):
        pass

    def update_all_available_moves(self):
        pass




class Whites(Opponent):
    def correct_fig_name(self):
        pass


class Blacks(Opponent):
    def correct_fig_name(self, figure):
        figure.name = self.name.lower()


