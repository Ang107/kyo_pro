import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Path to the directory containing input files
input_dir = "tools/in/"

# Number of files
num_files = 100

# Create a figure for each file and plot the target points
for idx in range(num_files):
    file_path = os.path.join(input_dir, f"{idx:04}.txt")
    if not os.path.isfile(file_path):
        continue

    # Read the file
    with open(file_path, "r") as f:
        lines = f.readlines()

    # Parse header: N K H T D
    header = lines[0].split()
    N, K, H, T, D = map(int, header)

    # Skip K lines of own colors
    start = 1 + K

    # Extract H target points (CMY)
    targets = []
    for i in range(start, start + H):
        c, m, y = map(float, lines[i].split())
        targets.append((c, m, y))
    targets = np.array(targets)

    # Plot
    fig = plt.figure(figsize=(6, 5))
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(targets[:, 0], targets[:, 1], targets[:, 2], c="blue", s=2)
    ax.set_title(f"Targets for file index {idx:04}")
    ax.set_xlabel("C")
    ax.set_ylabel("M")
    ax.set_zlabel("Y")
    plt.tight_layout()
    plt.show()
