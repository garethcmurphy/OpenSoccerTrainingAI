#!/usr/bin/env python3
"""
Setup some standard cone layouts
like zigzag, diagonal, square, etc.
"""
from draw_cone_layout import ConeLayoutDrawer


class ConeLayoutSetup:
    """Class to setup different cone layouts"""

    def __init__(self, filename="cone_layout.png"):
        self.filename = filename

    def setup_zigzag(self):
        cone_positions = [(i * 10, i * 10) for i in range(10)]
        self._draw_and_save(cone_positions, "zigzag_layout.png")

    def setup_diagonal(self):
        cone_positions = [(i, i) for i in range(10)]
        self._draw_and_save(cone_positions, "diagonal_layout.png")

    def setup_row(self):
        cone_positions = [(i, 20) for i in range(10)]
        self._draw_and_save(cone_positions, "row_layout.png")

    def setup_column(self):
        cone_positions = [(20, i) for i in range(10)]
        self._draw_and_save(cone_positions, "column_layout.png")

    def setup_square(self):
        cone_positions = [
            (0, 0),
            (0, 1),
            (1, 0),
            (1, 1),
            (2, 0),
            (2, 1),
            (3, 0),
            (3, 1),
            (4, 0),
            (4, 1),
            (5, 0),
            (5, 1),
            (6, 0),
            (6, 1),
            (7, 0),
            (7, 1),
            (8, 0),
            (8, 1),
            (9, 0),
            (9, 1),
        ]
        self._draw_and_save(cone_positions, "square_layout.png")

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
