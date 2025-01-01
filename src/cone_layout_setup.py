#!/usr/bin/env python3
"""
Setup some standard cone layouts
like zigzag, diagonal, square, etc.
for turning, shooting, dribbling,
and agility drills.
"""

import math

from cone_layout_drawer import ConeLayoutDrawer

# Constants
ZIGZAG_START_X = 25
ZIGZAG_START_Y = 15
ZIGZAG_STEP_X = 6
ZIGZAG_STEP_Y = 12
DIAGONAL_STEP = 6
ROW_Y = 20
ROW_STEP = 4
COLUMN_X = 15
COLUMN_STEP = 4
SQUARE_SIDE_LENGTH = 15
NUM_CONES = 10


class ConeLayoutSetup:
    """Class to setup different cone layouts"""

    def __init__(self, filename="cone_layout.png"):
        self.filename = filename

    def setup_zigzag(self):
        """Dribble Drill (Zigzag)"""
        cone_positions = [
            (
                ZIGZAG_START_X + i * ZIGZAG_STEP_X,
                ZIGZAG_START_Y + (i % 2) * ZIGZAG_STEP_Y - ZIGZAG_STEP_Y / 2,
            )
            for i in range(NUM_CONES)
        ]
        self._draw_and_save(
            cone_positions,
            "zigzag_layout.png",
            "Dribble Drill (Zigzag)",
        )

    def setup_diagonal(self):
        """Shooting Drill (Diagonal Layout)"""
        cone_positions = [
            (i * DIAGONAL_STEP, i * DIAGONAL_STEP) for i in range(NUM_CONES)
        ]
        self._draw_and_save(
            cone_positions,
            "diagonal_layout.png",
            "Diagonal Layout",
        )

    def setup_row(self):
        """Agility Drill (Row Layout)"""
        cone_positions = [(5 + i * ROW_STEP, ROW_Y) for i in range(NUM_CONES)]
        self._draw_and_save(
            cone_positions,
            "row_layout.png",
            "Row Layout",
        )

    def setup_column(self):
        """Agility Drill (Column Layout)"""
        cone_positions = [
            (
                COLUMN_X,
                5 + i * COLUMN_STEP,
            )
            for i in range(NUM_CONES)
        ]
        self._draw_and_save(
            cone_positions,
            "column_layout.png",
            "Agility Drill (Column Layout)",
        )

    def setup_square(self):
        """Turning Drill (Square)"""
        cone_positions = []
        for x in range(SQUARE_SIDE_LENGTH):
            cone_positions.append((x, 0))
            cone_positions.append((x, SQUARE_SIDE_LENGTH - 1))
        for y in range(1, SQUARE_SIDE_LENGTH - 1):
            cone_positions.append((0, y))
            cone_positions.append((SQUARE_SIDE_LENGTH - 1, y))
        self._draw_and_save(
            cone_positions,
            "hollow_square_layout.png",
            "Turning Drill (Square)",
        )

    def circle_layout(self):
        """Agility Drill (Circle Layout)"""
        cone_positions = []
        for i in range(0, 360, 10):
            cone_positions.append(
                (10 * math.cos(math.radians(i)), 10 * math.sin(math.radians(i)))
            )
        self._draw_and_save(
            cone_positions,
            "circle_layout.png",
            "Agility Drill Circle Layout",
        )

    def _draw_and_save(self, cone_positions, filename, title):
        """Draw and save the cone layout"""
        drawer = ConeLayoutDrawer(
            cone_positions,
            "./src/assets/images/" + filename,
            title,
        )
        drawer.save_plot()


if __name__ == "__main__":
    layout_setup = ConeLayoutSetup()
    layout_setup.setup_zigzag()
    layout_setup.setup_diagonal()
    layout_setup.setup_row()
    layout_setup.setup_column()
    layout_setup.setup_square()
