"""
Use a stack to keep a monotonically decreasing series

if top < newItem, pop the top and update it, repeat until the top is greater than the newTtem
else, push newItem to stack

Time: O(n)- one pass
Space: O(n)
"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # element: [temp, idx]

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                _, idx = stack.pop()
                res[idx] = i-idx
            
            stack.append([t, i])
        
        return res




