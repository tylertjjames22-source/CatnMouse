from carnivore import Carnivore
from mouse import Mouse


class Cat(Carnivore):
    """A cat: chases mice one space per step (diagonals allowed) and naps when full."""

    def __init__(
        self,
        x,
        y,
        board,
        meals_to_satisfy=2,
        image="images/cat-temp.png",
        sleeping_image="images/cat-sleeping.png",
    ):
        super().__init__(x, y, board, Mouse, image, sleeping_image, meals_to_satisfy)
