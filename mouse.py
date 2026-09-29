import random

from board_object import BoardObject
from board_utils import in_bounds


class Mouse(BoardObject):
    """A mouse that wanders randomly, one space per step, and never leaves the board."""

    DIRECTIONS = [(dx, dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1) if (dx, dy) != (0, 0)]

    def __init__(self, x, y, board, image="images/mouse-temp.png"):
        super().__init__()
        self.x = x
        self.y = y
        self.board = board  # needed so the mouse can ask how big the board is
        self.image = image

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_image(self):
        return self.image

    def move_to_if_legal(self, new_x, new_y):
        """Move to (new_x, new_y) unless it is off the board, in which case stay put."""
        if in_bounds(self.board, new_x, new_y):
            self.x = new_x
            self.y = new_y

    def step(self):
        dx, dy = random.choice(self.DIRECTIONS)
        self.move_to_if_legal(self.x + dx, self.y + dy)
