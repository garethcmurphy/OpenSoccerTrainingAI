#!/usr/bin/env python3
"""Request llm google gemini
to create drills example"""


class Drill:
    def __init__(self, name, description, duration):
        self.name = name
        self.description = description
        self.duration = duration

    def __str__(self):
        return f"{self.name} ({self.duration} minutes): {self.description}"


class DrillSet:
    def __init__(self):
        self.drills = []

    def add_drill(self, drill):
        self.drills.append(drill)

    def __str__(self):
        return "\n".join(str(drill) for drill in self.drills)


def main():
    drills = DrillSet()
    drills.add_drill(Drill("Passing drills", "Improve passing accuracy", 60))
    drills.add_drill(
        Drill(
            "Shooting drills",
            "Work on shooting technique",
            90,
        )
    )
    drills.add_drill(Drill("1v1 drills", "Enhance dribbling skills", 120))

    print(drills)


if __name__ == "__main__":
    main()
