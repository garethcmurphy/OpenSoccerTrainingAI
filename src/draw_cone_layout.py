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
PITCH_COLOR = "#228B22"
BACKGROUND_COLOR = "white"
CONE_COLOR = "orange"
CONE_SIZE = 200
CONE_MARKER = "^"
PITCH_LENGTH = 105
PITCH_WIDTH = 68
PITCH_DIMENSIONS = (PITCH_LENGTH, PITCH_WIDTH)
PENALTY_SPOT_POSITIONS = [(11, PITCH_WIDTH / 2), (PITCH_LENGTH - 11, PITCH_WIDTH / 2)]
LINE_WIDTH = 2
CENTER_CIRCLE_RADIUS = 9.15
CENTER_SPOT_RADIUS = 0.8
PENALTY_AREA_WIDTH = 40.3
PENALTY_AREA_DEPTH = 16.5
GOAL_AREA_WIDTH = 18.32
GOAL_AREA_DEPTH = 5.5
PENALTY_SPOT_RADIUS = 0.8
GOAL_WIDTH = 7.32
GOAL_DEPTH = 0.5
PENALTY_ARC_RADIUS = 9.15
HALFWAY_LINE_COORDS = ([PITCH_LENGTH / 2, PITCH_LENGTH / 2], [0, PITCH_WIDTH])


class ConeLayoutDrawer:
    """Cone layout drawer class"""

    def __init__(self, cone_positions, filename="cone_layout.png"):
        self.cone_positions = cone_positions
        self.filename = filename
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
        for x, y in self.cone_positions:
            self.ax.scatter(
                x,
                y,
                color=CONE_COLOR,
                s=CONE_SIZE,
                marker=CONE_MARKER,
            )

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
            (PITCH_LENGTH / 2, PITCH_WIDTH / 2),
            CENTER_CIRCLE_RADIUS,
            color="white",
            fill=False,
        )
        self.ax.add_artist(center_circle)

    def draw_center_spot(self):
        center_spot = plt.Circle(
            (PITCH_LENGTH / 2, PITCH_WIDTH / 2), CENTER_SPOT_RADIUS, color="white"
        )
        self.ax.add_artist(center_spot)

    def draw_penalty_areas(self):
        penalty_area = patches.Rectangle(
            (0, (PITCH_WIDTH - PENALTY_AREA_WIDTH) / 2),
            PENALTY_AREA_DEPTH,
            PENALTY_AREA_WIDTH,
            linewidth=LINE_WIDTH,
            edgecolor="white",
            facecolor="none",
        )
        self.ax.add_patch(penalty_area)
        penalty_area = patches.Rectangle(
            (PITCH_LENGTH - PENALTY_AREA_DEPTH, (PITCH_WIDTH - PENALTY_AREA_WIDTH) / 2),
            PENALTY_AREA_DEPTH,
            PENALTY_AREA_WIDTH,
            linewidth=LINE_WIDTH,
            edgecolor="white",
            facecolor="none",
        )
        self.ax.add_patch(penalty_area)

    def draw_goal_areas(self):
        goal_area = patches.Rectangle(
            (0, (PITCH_WIDTH - GOAL_AREA_WIDTH) / 2),
            GOAL_AREA_DEPTH,
            GOAL_AREA_WIDTH,
            linewidth=LINE_WIDTH,
            edgecolor="white",
            facecolor="none",
        )
        self.ax.add_patch(goal_area)
        goal_area = patches.Rectangle(
            (PITCH_LENGTH - GOAL_AREA_DEPTH, (PITCH_WIDTH - GOAL_AREA_WIDTH) / 2),
            GOAL_AREA_DEPTH,
            GOAL_AREA_WIDTH,
            linewidth=LINE_WIDTH,
            edgecolor="white",
            facecolor="none",
        )
        self.ax.add_patch(goal_area)

    def draw_penalty_spots(self):
        penalty_spot = plt.Circle(
            PENALTY_SPOT_POSITIONS[0],
            PENALTY_SPOT_RADIUS,
            color="white",
        )
        self.ax.add_artist(penalty_spot)
        penalty_spot = plt.Circle(
            PENALTY_SPOT_POSITIONS[1],
            PENALTY_SPOT_RADIUS,
            color="white",
        )
        self.ax.add_artist(penalty_spot)

    def draw_goals(self):
        goal = patches.Rectangle(
            (0, (PITCH_WIDTH - GOAL_WIDTH) / 2),
            GOAL_DEPTH,
            GOAL_WIDTH,
            linewidth=LINE_WIDTH,
            edgecolor="white",
            facecolor="white",
        )
        self.ax.add_patch(goal)
        goal = patches.Rectangle(
            (PITCH_LENGTH - GOAL_DEPTH, (PITCH_WIDTH - GOAL_WIDTH) / 2),
            GOAL_DEPTH,
            GOAL_WIDTH,
            linewidth=LINE_WIDTH,
            edgecolor="white",
            facecolor="white",
        )
        self.ax.add_patch(goal)

    def draw_penalty_arcs(self):
        penalty_arc = patches.Arc(
            (11, PITCH_WIDTH / 2),
            2 * PENALTY_ARC_RADIUS,
            2 * PENALTY_ARC_RADIUS,
            angle=0,
            theta1=300,
            theta2=60,
            linewidth=LINE_WIDTH,
            edgecolor="white",
        )
        self.ax.add_patch(penalty_arc)
        penalty_arc = patches.Arc(
            (PITCH_LENGTH - 11, PITCH_WIDTH / 2),
            2 * PENALTY_ARC_RADIUS,
            2 * PENALTY_ARC_RADIUS,
            angle=0,
            theta1=120,
            theta2=240,
            linewidth=LINE_WIDTH,
            edgecolor="white",
        )
        self.ax.add_patch(penalty_arc)

    def draw_halfway_line(self):
        halfway_line = plt.Line2D(*HALFWAY_LINE_COORDS, color="white")
        self.ax.add_artist(halfway_line)

    def set_labels(self):
        self.ax.set_xlim(0, PITCH_LENGTH)
        self.ax.set_ylim(0, PITCH_WIDTH)
        self.ax.set_title("Football Pitch with Orange Cones")
        self.ax.set_xlabel("Length")
        self.ax.set_ylabel("Width")

    def save_plot(self):
        plt.savefig(self.filename)


if __name__ == "__main__":
    cone_positions = [(10, 10), (20, 40), (30, 20), (50, 25), (70, 35), (90, 10)]
    drawer = ConeLayoutDrawer(cone_positions, "cone_layout.png")
    drawer.save_plot()
