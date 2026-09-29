from board_utils import chebyshev_distance
from cat import Cat


class SmartCat(Cat):
    """A cat that always chases the *closest* mouse instead of just the first one."""

    def __init__(self, x, y, board, meals_to_satisfy=3):
        super().__init__(
            x,
            y,
            board,
            meals_to_satisfy,
            image="images/smart-cat.png",
            sleeping_image="images/smart-cat-sleeping.png",
        )

    def choose_prey(self, candidates):
        if not candidates:
            return None
        return min(candidates, key=lambda m: chebyshev_distance(self, m))
