class BoardObject:
    """A general object in the simulation. Subclasses override all four methods."""

    def get_x(self):
        raise NotImplementedError

    def get_y(self):
        raise NotImplementedError

    def get_image(self):
        raise NotImplementedError

    def step(self):
        raise NotImplementedError