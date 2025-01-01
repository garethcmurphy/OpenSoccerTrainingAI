#!/usr/bin/env python3
"""
Python class to setup drills for cone layout drawing.
"""

from typing import List, Tuple

import pydantic


class Drill(pydantic.BaseModel):
    cone_positions: List[Tuple[int, int]]
    calories: int
    time_taken: int
    effort: str
    filename: str

    class Config:
        arbitrary_types_allowed = True

    def __str__(self):
        return f"""
Drill with {self.calories} calories,
{self.time_taken} minutes, {self.effort} effort,
and cone layout saved as {self.filename}
"""


class DrillManager:
    def __init__(self, drills: List[Drill]):
        self.drills = drills

    def __str__(self):
        return "\n".join(str(drill) for drill in self.drills)


def main():
    drills_data = [
        {
            "cone_positions": [
                (10, 10),
                (20, 40),
                (30, 20),
                (50, 25),
                (70, 35),
                (90, 10),
            ],
            "calories": 100,
            "time_taken": 30,
            "effort": "high",
            "filename": "cone_layout1.png",
        },
        {
            "cone_positions": [
                (15, 15),
                (25, 45),
                (35, 25),
                (55, 30),
                (75, 40),
                (95, 15),
            ],
            "calories": 120,
            "time_taken": 35,
            "effort": "medium",
            "filename": "cone_layout2.png",
        },
        {
            "cone_positions": [
                (5, 5),
                (15, 35),
                (25, 15),
                (45, 20),
                (65, 30),
                (85, 5),
            ],
            "calories": 90,
            "time_taken": 25,
            "effort": "low",
            "filename": "cone_layout3.png",
        },
    ]

    drills = DrillManager([Drill(**data) for data in drills_data])
    print(drills)


if __name__ == "__main__":
    main()
