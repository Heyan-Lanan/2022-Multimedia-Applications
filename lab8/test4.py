import cv2
import numpy as np

moon = cv2.imread("test2.jpg", 0)
row, column = moon.shape
gradient = np.empty((row, column), dtype=str)
value = np.empty((row, column), dtype=int)
vector_value = np.empty(row, dtype=int)
vector_dir = np.empty(row, dtype=str)

for x in range(1, row - 1):
    for y in range(1, column - 1):
        top_left = int(moon[x, y]) - int(moon[x - 1, y - 1])
        top = int(moon[x, y]) - int(moon[x, y - 1])
        top_right = int(moon[x, y]) - int(moon[x + 1, y - 1])
        right = int(moon[x, y]) - int(moon[x + 1, y])
        bottom_right = int(moon[x, y]) - int(moon[x + 1, y + 1])
        bottom = int(moon[x, y]) - int(moon[x, y + 1])
        bottom_left = int(moon[x, y]) - int(moon[x - 1, y + 1])
        left = int(moon[x, y]) - int(moon[x - 1, y])
        max_dir = max(top_left, top, top_right, right, bottom_right, bottom, bottom_left, left)
        value[x][y] = max_dir
        if max_dir == top_left:
            gradient[x][y] = "↖"
        elif max_dir == top:
            gradient[x][y] = "↑"
        elif max_dir == top_right:
            gradient[x][y] = "↗"
        elif max_dir == right:
            gradient[x][y] = "→"
        elif max_dir == bottom_right:
            gradient[x][y] = "↘"
        elif max_dir == bottom:
            gradient[x][y] = "↓"
        elif max_dir == bottom_left:
            gradient[x][y] = "↙"
        else:
            gradient[x][y] = "←"

for j in range(row):
    max_value = -10000000
    max_dir = ""
    for i in range(column):
        if value[j][i] > max_value:
            max_value = value[j][i]
            max_dir = gradient[j][i]
    vector_value[j] = max_value
    vector_dir[j] = max_dir

for j in range(row):
    print(j, '(', vector_value[j], ',', vector_dir[j], ')')
for item1 in gradient:
    # for item2 in item1:
    print(item1)
