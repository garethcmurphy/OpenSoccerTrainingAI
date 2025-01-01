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
    drills.add_drill(Drill("Fitness drills", "Improve stamina and speed", 45))
    drills.add_drill(Drill("Defensive drills", "Enhance defensive skills", 60))
    drills.add_drill(Drill("Attacking drills", "Enhance attacking skills", 60))
    drills.add_drill(
        Drill(
            "Goalkeeping drills",
            "Enhance goalkeeping skills",
            60,
        )
    )
    drills.add_drill(Drill("Tactical drills", "Enhance tactical skills", 60))
    drills.add_drill(Drill("Set-piece drills", "Enhance set-piece skills", 60))
    drills.add_drill(
        Drill(
            "Conditioning drills",
            "Enhance conditioning skills",
            60,
        )
    )
    drills.add_drill(Drill("Recovery drills", "Enhance recovery skills", 60))
    drills.add_drill(Drill("Warm-up drills", "Enhance warm-up skills", 60))
    drills.add_drill(Drill("Cool-down drills", "Enhance cool-down skills", 60))
    drills.add_drill(Drill("Technical drills", "Enhance technical skills", 60))
    drills.add_drill(Drill("Physical drills", "Enhance physical skills", 60))
    drills.add_drill(Drill("Mental drills", "Enhance mental skills", 60))
    drills.add_drill(Drill("Speed drills", "Enhance speed skills", 60))
    drills.add_drill(Drill("Agility drills", "Enhance agility skills", 60))
    drills.add_drill(Drill("Strength drills", "Enhance strength skills", 60))
    drills.add_drill(Drill("Power drills", "Enhance power skills", 60))
    drills.add_drill(Drill("Endurance drills", "Enhance endurance skills", 60))

    print(drills)


if __name__ == "__main__":
    main()
