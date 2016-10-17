class Opponent(object):
    def __init__(self, board, opponent=None, level=1):
        self.occupation = set()  # cells
        self.board = board
        self.figures = []
        self.avail_moves = set()
        self.priority_move_queue = []
        self.opponent = opponent
        self.level = level

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

    # TODO
    # redesign priority_map based on level of the gamer
    # higher the level - more moves further
    # the gamer should "think"
    def make_priority_moves_map(self, level):
        move_values = {'kill' :  {'q': float('inf'),
                                  'r': 15,
                                  'b': 9,
                                  'k': 9},
                       'save' :  {'q': 100,
                                  'r': 10,
                                  'b': 5,
                                  'k': 5},
                       'attack': {'q': 8,
                                  'r': 3,
                                  'b': 1,
                                  'k': 1},
                       }

        self.priority_move_queue = []

        move_idx = 0
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
                attack_opportunity = figure.check_move(move) & self.opponent.occupation
                for attack in attack_opportunity:
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
                # move_points += len(figure.check_move(move))/2
                move_summary = (move_points, move_idx, figure, move)
                self.priority_move_queue.append(move_summary)
                move_idx += 1
                # print(move_summary)

        self.priority_move_queue = sorted(self.priority_move_queue, reverse=True)

    # TODO
    def make_best_move(self):
        self.make_priority_moves_map()
        *_, figure, to_cell = self.priority_move_queue.pop(0)
        print(figure.name, figure.cell, to_cell)
        self.remove_figure(figure)
        if to_cell in self.opponent.occupation:
            self.opponent.remove_figure(self.board.get_figure(to_cell))
        figure.cell = to_cell
        figure.avail_moves = figure.get_avail_moves() - {figure.cell}
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
