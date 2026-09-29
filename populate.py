import random

from board_utils import add_object, get_dimensions
from cat import Cat
from hippopotamus import Hippopotamus
from mouse import Mouse
from mouse_den import MouseDen
from smart_cat import SmartCat
from smart_mouse import SmartMouse


def populate(board):
    """Fill the board with a bit of everything. Call this from main.py."""
    width, height = get_dimensions(board)

    def spot():
        return random.randrange(width), random.randrange(height)

    for _ in range(6):
        add_object(board, Mouse(*spot(), board))
    for _ in range(3):
        add_object(board, SmartMouse(*spot(), board))
    add_object(board, Cat(*spot(), board))
    add_object(board, SmartCat(*spot(), board))
    add_object(board, Hippopotamus(*spot(), board))
    add_object(board, MouseDen(*spot(), board, spawn_class=SmartMouse))
