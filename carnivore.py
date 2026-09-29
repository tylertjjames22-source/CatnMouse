from board_object import BoardObject
from board_utils import remove_object, sign


class Carnivore(BoardObject):
    """Base class for anything that chases and eats other board objects.

    Subclasses customise behaviour by passing different constructor arguments or by
    overriding one of the small hook methods:

        is_edible(obj)         - which objects count as food
        choose_prey(cands)     - which of the edible objects to chase
        ready_to_act()         - whether this step is an "active" step
        choose_direction(prey) - which way to move toward the prey
    """

    def __init__(self, x, y, board, prey_type, image, sleeping_image, meals_to_satisfy=1):
        super().__init__()
        self.x = x
        self.y = y
        self.board = board
        self.prey_type = prey_type          # a class, e.g. Mouse
        self.image = image
        self.sleeping_image = sleeping_image
        self.meals_to_satisfy = meals_to_satisfy
        self.meals_eaten = 0

    # ---- BoardObject interface ----
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_image(self):
        return self.sleeping_image if self.is_satisfied() else self.image

    # ---- appetite ----
    def is_satisfied(self):
        return self.meals_eaten >= self.meals_to_satisfy

    def eat(self, prey):
        remove_object(self.board, prey)
        self.meals_eaten += 1

    # ---- choosing prey ----
    def is_edible(self, obj):
        """True if obj is an instance of prey_type, isn't this carnivore, and can be eaten."""
        return (
            obj is not self
            and isinstance(obj, self.prey_type)
            and getattr(obj, "edible", True)
        )

    def choose_prey(self, candidates):
        """Pick one of the edible objects (default: the first). Override for smarter choices."""
        return candidates[0] if candidates else None

    def get_prey(self):
        """Return an object of prey_type from the board, or None if there is none."""
        candidates = [o for o in self.board.get_board_objects() if self.is_edible(o)]
        return self.choose_prey(candidates)

    # ---- pacing and movement ----
    def ready_to_act(self):
        """Called once per step; return False to skip this step entirely."""
        return True

    def choose_direction(self, prey):
        """Return (dx, dy) toward the prey; x and y are handled independently (diagonals OK)."""
        return sign(prey.get_x() - self.x), sign(prey.get_y() - self.y)

    def move_toward(self, prey):
        dx, dy = self.choose_direction(prey)
        self.x += dx
        self.y += dy

    def on_same_space(self, other):
        return self.x == other.get_x() and self.y == other.get_y()

    def step(self):
        if self.is_satisfied():
            return
        if not self.ready_to_act():
            return
        prey = self.get_prey()
        if prey is None:
            return
        if self.on_same_space(prey):
            self.eat(prey)
        else:
            self.move_toward(prey)
