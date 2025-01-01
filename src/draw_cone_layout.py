#!/usr/bin/env python3
"""
Draw cone layout using matplotlib
with green background and orange cones
for multiple drills
"""
import matplotlib.patches as patches
import matplotlib.pyplot as plt

# Constants
FIG_SIZE = (8, 5)
PITCH_COLOR = "green"
BACKGROUND_COLOR = "white"
CONE_COLOR = "orange"
CONE_SIZE = 200
CONE_MARKER = "^"
CONE_POSITIONS = [(10, 10), (20, 40), (30, 20), (50, 25), (70, 35), (90, 10)]
PITCH_DIMENSIONS = (100, 50)
LINE_WIDTH = 2
CENTER_CIRCLE_RADIUS = 9.15
CENTER_SPOT_RADIUS = 0.8
PENALTY_AREA_DIMENSIONS = (16, 18)
GOAL_AREA_DIMENSIONS = (6, 14)
PENALTY_SPOT_RADIUS = 0.8
GOAL_DIMENSIONS = (0.5, 6)
PENALTY_ARC_DIMENSIONS = (18.3, 18.3)
HALFWAY_LINE_COORDS = ([50, 50], [0, 50])


class ConeLayoutDrawer:
    """cone layout drawer class"""

    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=FIG_SIZE)
        self.setup_pitch()

    def setup_pitch(self):
        self.fig.patch.set_facecolor(BACKGROUND_COLOR)
        self.ax.set_facecolor(BACKGROUND_COLOR)
        self.draw_pitch()
        self.draw_cones()
        self.draw_lines()
        self.set_labels()

    def draw_pitch(self):
        pitch = patches.Rectangle(
            (0, 0),
            *PITCH_DIMENSIONS,
            linewidth=LINE_WIDTH,
            edgecolor="black",
            facecolor=PITCH_COLOR,
        )
        self.ax.add_patch(pitch)

    def draw_cones(self):
        for x, y in CONE_POSITIONS:
            self.ax.scatter(x, y, color=CONE_COLOR, s=CONE_SIZE, marker=CONE_MARKER)

    def draw_lines(self):
        self.draw_center_circle()
        self.draw_center_spot()
        self.draw_penalty_areas()
        self.draw_goal_areas()
        self.draw_penalty_spots()
        self.draw_goals()
        self.draw_penalty_arcs()
        self.draw_halfway_line()

    def draw_center_circle(self):
        center_circle = plt.Circle(
            (50, 25), CENTER_CIRCLE_RADIUS, color="white", fill=False
        )
        self.ax.add_artist(center_circle)

    def draw_center_spot(self):
        center_spot = plt.Circle((50, 25), CENTER_SPOT_RADIUS, color="white")
        self.ax.add_artist(center_spot)

    def draw_penalty_areas(self):
        penalty_area = patches.Rectangle(
            (0, 16),
            *PENALTY_AREA_DIMENSIONS,
            linewidth=LINE_WIDTH,
            edgecolor="white",
            facecolor="none",
        )
        self.ax.add_patch(penalty_area)
        penalty_area = patches.Rectangle(
            (100 - PENALTY_AREA_DIMENSIONS[0], 16),
            *PENALTY_AREA_DIMENSIONS,
            linewidth=LINE_WIDTH,
            edgecolor="white",
            facecolor="none",
        )
        self.ax.add_patch(penalty_area)

    def draw_goal_areas(self):
        goal_area = patches.Rectangle(
            (0, 18),
            *GOAL_AREA_DIMENSIONS,
            linewidth=LINE_WIDTH,
            edgecolor="white",
            facecolor="none",
        )
        self.ax.add_patch(goal_area)
        goal_area = patches.Rectangle(
            (100 - GOAL_AREA_DIMENSIONS[0], 18),
            *GOAL_AREA_DIMENSIONS,
            linewidth=LINE_WIDTH,
            edgecolor="white",
            facecolor="none",
        )
        self.ax.add_patch(goal_area)

    def draw_penalty_spots(self):
        penalty_spot = plt.Circle((12, 25), PENALTY_SPOT_RADIUS, color="white")
        self.ax.add_artist(penalty_spot)
        penalty_spot = plt.Circle((100 - 12, 25), PENALTY_SPOT_RADIUS, color="white")
        self.ax.add_artist(penalty_spot)

    def draw_goals(self):
        goal = patches.Rectangle(
            (0, 22),
            *GOAL_DIMENSIONS,
            linewidth=LINE_WIDTH,
            edgecolor="white",
            facecolor="white",
        )
        self.ax.add_patch(goal)
        goal = patches.Rectangle(
            (100 - GOAL_DIMENSIONS[0], 22),
            *GOAL_DIMENSIONS,
            linewidth=LINE_WIDTH,
            edgecolor="white",
            facecolor="white",
        )
        self.ax.add_patch(goal)

    def draw_penalty_arcs(self):
        penalty_arc = patches.Arc(
            (12, 25),
            *PENALTY_ARC_DIMENSIONS,
            angle=0,
            theta1=308,
            theta2=52,
            linewidth=LINE_WIDTH,
            edgecolor="white",
        )
        self.ax.add_patch(penalty_arc)
        penalty_arc = patches.Arc(
            (100 - 12, 25),
            *PENALTY_ARC_DIMENSIONS,
            angle=0,
            theta1=128,
            theta2=232,
            linewidth=LINE_WIDTH,
            edgecolor="white",
        )
        self.ax.add_patch(penalty_arc)

    def draw_halfway_line(self):
        halfway_line = plt.Line2D(*HALFWAY_LINE_COORDS, color="white")
        self.ax.add_artist(halfway_line)

    def set_labels(self):
        self.ax.set_xlim(0, 100)
        self.ax.set_ylim(0, 50)
        self.ax.set_title("Football Pitch with Orange Cones")
        self.ax.set_xlabel("Length")
        self.ax.set_ylabel("Width")

    def save_plot(self, filename="cone_layout.png"):
        plt.savefig(filename)


if __name__ == "__main__":
    drawer = ConeLayoutDrawer()
    drawer.save_plot()
