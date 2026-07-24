"""
Use BFS to get connected components, then return the largest one

time: O(m*n)
space: O(m*n)
"""
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_area = 0
        visited = set()
        for r, row in enumerate(grid):
            for c, cell, in enumerate(row):
                if cell==0 or (r,c) in visited: continue

                # bfs
                q = deque()
                area = 0
                q.append((r, c))
                visited.add((r,c)) # mark the cell
                while q:
                    i, j = q.popleft()
                    area += 1

                    if i-1>=0 and (i-1,j) not in visited and grid[i-1][j]==1:
                        q.append((i-1,j))
                        visited.add((i-1,j)) # mark the cell
                    if j-1>=0 and (i,j-1) not in visited and grid[i][j-1]==1:
                        q.append((i,j-1))
                        visited.add((i,j-1)) # mark the cell
                    if i+1<m and (i+1,j) not in visited and grid[i+1][j]==1:
                        q.append((i+1,j))
                        visited.add((i+1,j)) # mark the cell
                    if j+1<n and (i,j+1) not in visited and grid[i][j+1]==1:
                        q.append((i,j+1))
                        visited.add((i,j+1)) # mark the cell
                max_area = max(max_area, area)
        return max_area

