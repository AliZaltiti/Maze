# =========================================================
#  Problem Solving Project
# Problem : Maze
# Written by: Ali Zeyad Ali Altiti
# =========================================================

import sys
sys.setrecursionlimit(10**7)

print("Welcome to Maze Program")
print("Written by: Ali Zeyad Ali Altiti\n")

# Read maze dimensions and number of cells to convert
n, m, k = map(int, input("Enter n, m and k: ").split())

# Read the maze
maze = [list(input()) for _ in range(n)]

visited = [[False]*m for _ in range(n)]
cells = []   # Stores empty cells in DFS order

# DFS function to visit all connected empty cells
def dfs(x, y):
    visited[x][y] = True
    cells.append((x, y))

    # Explore 4 possible directions
    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if maze[nx][ny] == '.' and not visited[nx][ny]:
                dfs(nx, ny)

# Start DFS from the first empty cell
for i in range(n):
    for j in range(m):
        if maze[i][j] == '.':
            dfs(i, j)
            break
    else:
        continue
    break

# Convert the last k visited cells into walls
for i in range(len(cells) - k, len(cells)):
    x, y = cells[i]
    maze[x][y] = 'X'

# Print the final maze
print("\nModified Maze:")
for row in maze:
    print("".join(row))
