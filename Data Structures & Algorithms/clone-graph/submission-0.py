"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

"""
Idea: Use a DFS-Like (recursive) way to 1. clone 2. Link the nodes
For each node in the given graph:
1. Clone the (val) if it's not been created, then "pre-collect the neighbors"
2. if a neighbor not yet created, create it then
-----------
use a dict with key and val both nodes
-----------
Time: O(V+E)
Space: O(V)
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node: return None
        
        old2new = dict()

        def cloning(node: Node)->Node:
            """
            the "input node" refers to the "old one"
            This will return the cloned node (new one)
            """
            if node in old2new:
                return old2new[node]
            
            # create new node and add it to the hashmap
            new_node = Node(node.val)
            old2new[node] = new_node

            # update the neighbors (recursively)
            for nei in node.neighbors:
                new_node.neighbors.append(cloning(nei))
            
            return new_node

        return cloning(node)





        