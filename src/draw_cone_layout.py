#!/usr/bin/env python3
"""Draw cone layout using matplotlib
with green background and orange cones
for multiple drills"""

import matplotlib.pyplot as plt

from setup_drills import Drill, DrillSet

# Sample drills
drills = DrillSet()
drills.add_drill(Drill("Passing drills", "Improve passing accuracy", 60))
drills.add_drill(Drill("Shooting drills", "Work on shooting technique", 90))
drills.add_drill(Drill("1v1 drills", "Enhance dribbling skills", 120))

# Cone layout for each drill
x = [0.1, 0.5, 1.5, 0.7]
y = [0.2, 1.5, 1.3, 0.5]
name = ["A", "B", "C", "D"]


def draw_cone_layout(drills):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_facecolor("green")
    for i in range(0, 4):
        ax.scatter(x[i], y[i], color="orange", s=1000)
        ax.text(x[i], y[i], name[i], color="black", ha="center", va="center")
    ax.set_xticks(range(3))
    ax.set_yticks(range(3))
    ax.set_xticklabels(["Left", "Center", "Right"])
    ax.set_yticklabels(["Back", "Middle", "Front"])
    ax.set_xlim(-0.5, 2.5)
    ax.set_ylim(2.5, -0.5)
    ax.set_title("Cone Layout for Drills")
    ax.set_aspect("equal")
    # set background green
    ax.set_facecolor("green")
    
    ax.axis("off")
    plt.tight_layout()
    plt.savefig("cone_layout.png")


if __name__ == "__main__":
    draw_cone_layout(drills)
