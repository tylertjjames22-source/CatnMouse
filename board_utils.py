"""Small helpers shared by the animal classes.

Everything that touches the Board API in a slightly "uncertain" way lives here,
so if the Board's signatures differ from what is assumed, only this file changes.
"""


def sign(n):
    """Return -1, 0, or 1 depending on the sign of n."""
    return (n > 0) - (n < 0)


def get_dimensions(board):
    """Return (width, height) of the board. Accepts a (w, h) pair or a single int."""
    size = board.get_size()
    if isinstance(size, (tuple, list)):
        return size[0], size[1]
    return size, size


def in_bounds(board, x, y):
    width, height = get_dimensions(board)
    return 0 <= x < width and 0 <= y < height


def chebyshev_distance(a, b):
    """Number of king-moves between two BoardObjects (diagonals count as 1)."""
    return max(abs(a.get_x() - b.get_x()), abs(a.get_y() - b.get_y()))


def add_object(board, obj):
    """Add one object to the board."""
    if hasattr(board, "add_board_object"):
        board.add_board_object(obj)
    else:
        board.add_board_objects([obj])


def remove_object(board, obj):
    """Remove one object from the board."""
    if hasattr(board, "remove_board_object"):
        board.remove_board_object(obj)
    else:
        board.remove_board_objects([obj])
