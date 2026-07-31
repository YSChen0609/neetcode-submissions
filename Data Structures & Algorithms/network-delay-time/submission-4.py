"""
Use Dijkstra Algo to get the shortest time to reach the "last node"
with a var to check if every node have received the signal

Time:O(ElogV)
Space: O(V**2)
"""

from collections import deque, defaultdict
import heapq as hq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # create the graph (adj list)
        adj = defaultdict(list)
        for u, v, t in times: adj[u].append([t, v])

        h = [[0,k]]
        visited = set()
        while h:
            cur_t, cur_v = hq.heappop(h)
            if cur_v in visited: continue
            visited.add(cur_v)
            if len(visited) == n: return cur_t

            for nei_t, nei_v in adj[cur_v]:
                hq.heappush(h,[nei_t+cur_t, nei_v])
        
        return -1
            








