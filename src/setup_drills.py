#!/usr/bin/env python3
"""
Python class to setup drills for cone layout drawing.
"""

import pydantic


class Drill(pydantic.BaseModel):
    cone_positions: list[tuple[int, int]]
    calories: int
    time_taken: int
    effort: str
    filename: str

    class Config:
        arbitrary_types_allowed = True


class Drills:
    def __init__(self, cone_positions, calories, time_taken, effort, filename):
        self.cone_positions = cone_positions
        self.calories = calories
        self.time_taken = time_taken
        self.effort = effort
        self.filename = filename

    def __str__(self):
        return f"""
Drill with {self.calories} calories, {self.time_taken}
minutes, {self.effort} effort,
and cone layout saved as {self.filename}
"""


def main():
    calories = 100
    time_taken = 30
    effort = "high"
    cone_positions = [
        (10, 10),
        (20, 40),
        (30, 20),
        (50, 25),
        (70, 35),
        (90, 10),
    ]
    filename = "cone_layout.png"
    drill = Drills(cone_positions, calories, time_taken, effort, filename)
    print(drill)


if __name__ == "__main__":
    main()
