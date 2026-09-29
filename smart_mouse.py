import random

from board_utils import in_bounds
from carnivore import Carnivore
from mouse import Mouse


class SmartMouse(Mouse):
    """A skittish mouse: wanders randomly, but runs from any carnivore within sight range."""

    def __init__(self, x, y, board, sight=4):
        super().__init__(x, y, board, image="images/smart-mouse.png")
        self.sight = sight

    def nearest_threat(self):
        threats = [o for o in self.board.get_board_objects() if isinstance(o, Carnivore)]
        threats = [t for t in threats if self.distance_sq(t) <= self.sight ** 2]
        return min(threats, key=self.distance_sq) if threats else None

    def distance_sq(self, other):
        return (self.x - other.get_x()) ** 2 + (self.y - other.get_y()) ** 2

    def step(self):
        threat = self.nearest_threat()
        if threat is None:
            super().step()  # nothing nearby: ordinary random wandering
            return

        # Consider every legal neighbouring square (and staying put); take the one
        # farthest from the threat, breaking ties randomly.
        options = [(self.x, self.y)]
        for dx, dy in self.DIRECTIONS:
            if in_bounds(self.board, self.x + dx, self.y + dy):
                options.append((self.x + dx, self.y + dy))

        def gap(pos):
            return (pos[0] - threat.get_x()) ** 2 + (pos[1] - threat.get_y()) ** 2

        best = max(gap(p) for p in options)
        self.x, self.y = random.choice([p for p in options if gap(p) == best])
