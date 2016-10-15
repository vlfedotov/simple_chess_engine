class Opponent(object):
    def __init__(self, board, opponent=None):
        self.occupation = set()  # cells
        self.board = board
        self.figures = []
        self.avail_moves = set()
        self.priority_move_queue = []
        self.opponent = opponent

    def setup_opponent(self, opponent):
        self.opponent = opponent

    def add_figure(self, figure):
        figure.name = self.correct_fig_name(figure)
        self.board.setup_fig(figure, figure.cell)
        self.figures.append(figure)
        self.occupation.add(figure.cell)
        self.update_all_available_moves()

    def remove_figure(self, figure):
        self.occupation.remove(figure.cell)
        self.figures.remove(figure)
        self.board.remove_fig(figure.cell)
        self.update_all_available_moves()

    def make_priority_moves_map(self):
        move_values = {'kill' :  {'q': float('inf'),
                                  'r': 70,
                                  'b': 60,
                                  'k': 60},
                       'save' :  {'q': 100,
                                  'r': 50,
                                  'b': 20,
                                  'k': 20},
                       'attack': {'q': 25,
                                  'r': 15,
                                  'b': 10,
                                  'k': 10},
                       'avail_moves': 'sdf',
                       }

        self.priority_move_queue = []

        for figure in self.figures:
            # print(figure.name)
            if figure.cell in self.opponent.avail_moves:
                figure.is_under_attack = True
                print(figure.name, 'is under attack')
            else:
                figure.is_under_attack = False

            for move in (figure.avail_moves - self.occupation):
                move_points = 0
                if move in self.opponent.occupation:

                    move_points += move_values['kill'][self.board.get_figure(move).name.lower()]
                    # print('kill', move, move_points)
                attack_oppontunity = figure.check_move(move) & self.opponent.occupation
                for attack in attack_oppontunity:
                    move_points += move_values['attack'][self.board.get_figure(attack).name.lower()]
                    # print('attack move', move, move_points)
                danger_move = move in self.opponent.avail_moves
                if danger_move:
                    move_points -= move_values['kill'][figure.name.lower()]
                    # print('danger move', move)
                if figure.is_under_attack:
                    save_opportunity = move not in self.opponent.avail_moves
                    if save_opportunity:
                        move_points += move_values['save'][figure.name.lower()]
                        # print('save move', move)
                move_points += len(figure.check_move(move))/2
                self.priority_move_queue.append((move_points, figure, move))

        self.priority_move_queue = sorted(self.priority_move_queue, reverse=True)

    # TODO
    def make_best_move(self):
        _, figure, to_cell = self.priority_move_queue.pop(0)
        self.remove_figure(figure)
        self.opponent.remove_figure(self.board.get_figure(to_cell))
        figure.cell = to_cell
        self.add_figure(figure)

    def update_all_available_moves(self):
        self.avail_moves = set()
        for figure in self.figures:
            self.avail_moves |= figure.avail_moves
        # TODO
        # if figures support each other
        # do not remove then
        for occ in self.occupation:
            self.avail_moves -= {occ}

    def correct_fig_name(self, figure):
        if isinstance(self, Blacks):
            return figure.name.lower()
        return figure.name


class Whites(Opponent):
    pass


class Blacks(Opponent):
    pass
