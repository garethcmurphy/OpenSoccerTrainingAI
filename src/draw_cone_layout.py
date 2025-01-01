#!/usr/bin/env python3
"""
Draw cone layout using matplotlib
with green background and orange cones
for multiple drills
"""
import matplotlib.patches as patches
import matplotlib.pyplot as plt

# Create a figure and axes
fig, ax = plt.subplots(figsize=(8, 5))

# Set the background color to white (football pitch-like)
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

# Draw the green pitch (plot area)
pitch = patches.Rectangle(
    (0, 0),
    100,
    50,
    linewidth=2,
    edgecolor="black",
    facecolor="green",
)
ax.add_patch(pitch)

# Add orange cones as scatter points
cone_positions = [(10, 10), (20, 40), (30, 20), (50, 25), (70, 35), (90, 10)]
for x, y in cone_positions:
    ax.scatter(
        x, y, color="orange", s=200, marker="^"
    )  # Orange cones with triangle markers

# Set limits and labels
ax.set_xlim(0, 100)
ax.set_ylim(0, 50)
ax.set_title("Football Pitch with Orange Cones")
ax.set_xlabel("Length")
ax.set_ylabel("Width")

# draw white soccer lines
# Center circle
center_circle = plt.Circle((50, 25), 9.15, color="white", fill=False)
ax.add_artist(center_circle)

# Center spot
center_spot = plt.Circle((50, 25), 0.8, color="white")
ax.add_artist(center_spot)

# Penalty area
penalty_area = patches.Rectangle(
    (0, 16), 16, 18, linewidth=2, edgecolor="white", facecolor="none"
)
ax.add_patch(penalty_area)
penalty_area = patches.Rectangle(
    (100 - 16, 16), 16, 18, linewidth=2, edgecolor="white", facecolor="none"
)
ax.add_patch(penalty_area)

# Goal area
goal_area = patches.Rectangle(
    (0, 18), 6, 14, linewidth=2, edgecolor="white", facecolor="none"
)
ax.add_patch(goal_area)
goal_area = patches.Rectangle(
    (100 - 6, 18), 6, 14, linewidth=2, edgecolor="white", facecolor="none"
)
ax.add_patch(goal_area)

# Penalty spot
penalty_spot = plt.Circle((12, 25), 0.8, color="white")
ax.add_artist(penalty_spot)
penalty_spot = plt.Circle((100 - 12, 25), 0.8, color="white")
ax.add_artist(penalty_spot)

# Goal
goal = patches.Rectangle(
    (0, 22), 0.5, 6, linewidth=2, edgecolor="white", facecolor="white"
)
ax.add_patch(goal)
goal = patches.Rectangle(
    (100 - 0.5, 22), 0.5, 6, linewidth=2, edgecolor="white", facecolor="white"
)
ax.add_patch(goal)

# Penalty arc
penalty_arc = patches.Arc(
    (12, 25),
    18.3,
    18.3,
    angle=0,
    theta1=308,
    theta2=52,
    linewidth=2,
    edgecolor="white",
)
ax.add_patch(penalty_arc)
penalty_arc = patches.Arc(
    (100 - 12, 25),
    18.3,
    18.3,
    angle=0,
    theta1=128,
    theta2=232,
    linewidth=2,
    edgecolor="white",
)
ax.add_patch(penalty_arc)

# Halfway line
halfway_line = plt.Line2D([50, 50], [0, 50], color="white")
ax.add_artist(halfway_line)


# Show the plot
plt.savefig("cone_layout.png")
