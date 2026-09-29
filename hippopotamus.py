from board_object import BoardObject
from carnivore import Carnivore


class Hippopotamus(Carnivore):
    """A hippo eats anything edible (except other hippos) but only acts every other step.

    Hippos lumber: they move along one axis at a time (whichever gap is bigger),
    never diagonally.
    """

    def __init__(
        self,
        x,
        y,
        board,
        meals_to_satisfy=5,
        image="images/hippo.png",
        sleeping_image="images/hippo-sleeping.png",
    ):
        super().__init__(x, y, board, BoardObject, image, sleeping_image, meals_to_satisfy)
        self.ticks = 0

    def is_edible(self, obj):
        return super().is_edible(obj) and not isinstance(obj, Hippopotamus)

    def ready_to_act(self):
        self.ticks += 1
        return self.ticks % 2 == 0

    def choose_direction(self, prey):
        gap_x = prey.get_x() - self.x
        gap_y = prey.get_y() - self.y
        if abs(gap_x) >= abs(gap_y):
            return (1 if gap_x > 0 else -1), 0
        return 0, (1 if gap_y > 0 else -1)
