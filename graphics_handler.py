import tkinter as tk


class GraphicsHandler:
    """Draws every board object at its (x, y) cell using the PNG its get_image() returns."""

    def __init__(self, width, height, cell_size=40, title="Cat and Mouse"):
        self.cell_size = cell_size
        self.root = tk.Tk()
        self.root.title(title)
        self.canvas = tk.Canvas(
            self.root,
            width=width * cell_size,
            height=height * cell_size,
            bg="#d8ecd0",
            highlightthickness=0,
        )
        self.canvas.pack()
        self._images = {}  # cache: path -> PhotoImage (must be kept alive or tkinter drops it)

    def _load(self, path):
        if path not in self._images:
            img = tk.PhotoImage(file=path)
            factor = max(1, round(max(img.width(), img.height()) / self.cell_size))
            self._images[path] = img.subsample(factor) if factor > 1 else img
        return self._images[path]

    def draw(self, objects):
        self.canvas.delete("all")
        half = self.cell_size // 2
        for obj in objects:
            cx = obj.get_x() * self.cell_size + half
            cy = obj.get_y() * self.cell_size + half
            self.canvas.create_image(cx, cy, image=self._load(obj.get_image()))
        self.root.update_idletasks()

    def after(self, delay_ms, callback):
        self.root.after(delay_ms, callback)

    def mainloop(self):
        self.root.mainloop()