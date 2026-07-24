"""
Use BFS to get connected components

1. for each cell, do:
    2. BFS to 4 directions, if reached all 0, ends, else, mark the visisted ones

time: O(n**2): all cell be reached at most once
space: O(n**2): the queue
"""

from collections import deque
class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:

        m, n = len(grid), len(grid[0])
        visited = set()
        res = 0
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == '0' or (r, c) in visited: continue

                # bfs
                res += 1
                q = deque()
                q.append((r, c)) # starting point
                while q:
                    i, j = q.popleft()
                    visited.add((i, j)) # mark the cell
                    print(i , j)
                    if i-1 >= 0 and (i-1, j) not in visited and grid[i-1][j]=='1':
                        q.append((i-1, j))
                        # visited.add((i-1, j))
                    if j-1 >= 0 and (i, j-1) not in visited and grid[i][j-1]=='1':
                        q.append((i, j-1))
                        # visited.add((i, j-1))
                    if i+1 < m and (i+1, j) not in visited and grid[i+1][j]=='1':
                        q.append((i+1, j))
                        # visited.add((i+1, j))
                    if j+1 < n and (i, j+1) not in visited and grid[i][j+1]=='1':
                        q.append((i, j+1))
                        # visited.add((i, j+1))
        return res
                







