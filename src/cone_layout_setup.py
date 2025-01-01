#!/usr/bin/env python3
"""
Setup some standard cone layouts
like zigzag, diagonal, square, etc.
"""
from cone_layout_drawer import ConeLayoutDrawer

# Constants
ZIGZAG_START_X = 25
ZIGZAG_START_Y = 15
ZIGZAG_STEP_X = 6
ZIGZAG_STEP_Y = 12
DIAGONAL_STEP = 6
ROW_Y = 20
ROW_STEP = 2
COLUMN_X = 20
COLUMN_STEP = 2
SQUARE_SIDE_LENGTH = 15
NUM_CONES = 10


class ConeLayoutSetup:
    """Class to setup different cone layouts"""

    def __init__(self, filename="cone_layout.png"):
        self.filename = filename

    def setup_zigzag(self):
        cone_positions = [
            (
                ZIGZAG_START_X + i * ZIGZAG_STEP_X,
                ZIGZAG_START_Y + (i % 2) * ZIGZAG_STEP_Y - ZIGZAG_STEP_Y / 2,
            )
            for i in range(NUM_CONES)
        ]
        self._draw_and_save(cone_positions, "zigzag_layout.png")

    def setup_diagonal(self):
        cone_positions = [
            (i * DIAGONAL_STEP, i * DIAGONAL_STEP) for i in range(NUM_CONES)
        ]
        self._draw_and_save(cone_positions, "diagonal_layout.png")

    def setup_row(self):
        cone_positions = [(i * ROW_STEP, ROW_Y) for i in range(NUM_CONES)]
        self._draw_and_save(cone_positions, "row_layout.png")

    def setup_column(self):
        cone_positions = [
            (
                COLUMN_X,
                i * COLUMN_STEP,
            )
            for i in range(NUM_CONES)
        ]
        self._draw_and_save(cone_positions, "column_layout.png")

    def setup_square(self):
        cone_positions = []
        for x in range(SQUARE_SIDE_LENGTH):
            cone_positions.append((x, 0))
            cone_positions.append((x, SQUARE_SIDE_LENGTH - 1))
        for y in range(1, SQUARE_SIDE_LENGTH - 1):
            cone_positions.append((0, y))
            cone_positions.append((SQUARE_SIDE_LENGTH - 1, y))
        self._draw_and_save(cone_positions, "hollow_square_layout.png")

    def _draw_and_save(self, cone_positions, filename):
        drawer = ConeLayoutDrawer(cone_positions, filename)
        drawer.save_plot()


if __name__ == "__main__":
    layout_setup = ConeLayoutSetup()
    layout_setup.setup_zigzag()
    layout_setup.setup_diagonal()
    layout_setup.setup_row()
    layout_setup.setup_column()
    layout_setup.setup_square()
