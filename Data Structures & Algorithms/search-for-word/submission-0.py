"""
use DFS with chr matching
1. From the first chr of the "word"
2. do bfs, if cannot match, return

Time: O(m*n * m*n)
Space: O(m*n) 
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        W_L = len(word)
        word_ptr = 0
        visited = set()
        DIR = [[0,1], [0,-1], [1,0], [-1, 0]]

        def dfs(ci:int,cj:int, word_ptr:int, cur_len: int) -> bool:
    
            if word_ptr >= W_L or board[ci][cj] != word[word_ptr]:
                return False
            if cur_len == W_L-1:
                return True 

            visited.add((ci,cj))

            for di, dj in DIR:
                new_i, new_j = ci+di, cj+dj
                if (new_i, new_j) not in visited and 0<=new_i<m and 0<=new_j<n:
                    if dfs(new_i, new_j, word_ptr+1, cur_len+1): return True
            
            visited.remove((ci,cj))

        
        for i in range(m):
            for j in range(n):
                visited.clear()
                if dfs(i,j,0,0): return True
            
        return False
        


