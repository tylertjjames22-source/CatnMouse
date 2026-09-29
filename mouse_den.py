from board_object import BoardObject
from board_utils import add_object
from mouse import Mouse


class MouseDen(BoardObject):
    """A stationary den that releases a new mouse every `spawn_interval` steps.

    It stops spawning once `max_mice` mice are alive, so the board can't overflow.
    Dens aren't animals, so carnivores ignore them (edible = False).
    """

    edible = False

    def __init__(self, x, y, board, spawn_interval=25, max_mice=10, spawn_class=Mouse):
        super().__init__()
        self.x = x
        self.y = y
        self.board = board
        self.spawn_interval = spawn_interval
        self.max_mice = max_mice
        self.spawn_class = spawn_class  # any Mouse subclass, e.g. SmartMouse
        self.ticks = 0

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_image(self):
        return "images/mouse-den.png"

    def mice_alive(self):
        return sum(isinstance(o, Mouse) for o in self.board.get_board_objects())

    def step(self):
        self.ticks += 1
        if self.ticks % self.spawn_interval == 0 and self.mice_alive() < self.max_mice:
            add_object(self.board, self.spawn_class(self.x, self.y, self.board))
