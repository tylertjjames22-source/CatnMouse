class Board:
    """Holds every BoardObject, steps them each tick, and asks the graphics to redraw.

    Origin (0, 0) is the top-left cell; x grows to the right and y grows downward.
    """

    def __init__(self, width=20, height=15, cell_size=40, delay_ms=150, graphics=None):
        self.width = width
        self.height = height
        self.delay_ms = delay_ms
        self.objects = []
        if graphics is None:
            from graphics_handler import GraphicsHandler  # imported here so tkinter is only needed to draw
            graphics = GraphicsHandler(width, height, cell_size)
        self.graphics = graphics

    def get_size(self):
        return (self.width, self.height)

    def get_board_objects(self):
        return list(self.objects)  # a copy, so callers can't modify the board by accident

    def add_board_objects(self, objs):
        self.objects.extend(objs)

    def remove_board_objects(self, objs):
        for obj in objs:
            if obj in self.objects:
                self.objects.remove(obj)

    def _tick(self):
        for obj in list(self.objects):
            if obj in self.objects:  # skip anything eaten earlier in this same tick
                obj.step()
        self.graphics.draw(self.objects)
        self.graphics.after(self.delay_ms, self._tick)

    def run_simulation(self):
        self._tick()
        self.graphics.mainloop()