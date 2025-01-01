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
        cone_positions = [(25 + i * 6, 15 + (i % 2) * 12 - 6) for i in range(10)]
        self._draw_and_save(cone_positions, "zigzag_layout.png")

    def setup_diagonal(self):
        cone_positions = [(i * 6, i * 6) for i in range(10)]
        self._draw_and_save(cone_positions, "diagonal_layout.png")

    def setup_row(self):
        cone_positions = [(i * 2, 20) for i in range(10)]
        self._draw_and_save(cone_positions, "row_layout.png")

    def setup_column(self):
        cone_positions = [(20, i * 2) for i in range(10)]
        self._draw_and_save(cone_positions, "column_layout.png")

    def setup_square(self):
        side_length = 15
        cone_positions = []
        for x in range(side_length):
            cone_positions.append((x, 0))
            cone_positions.append((x, side_length - 1))
        for y in range(1, side_length - 1):
            cone_positions.append((0, y))
            cone_positions.append((side_length - 1, y))
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
