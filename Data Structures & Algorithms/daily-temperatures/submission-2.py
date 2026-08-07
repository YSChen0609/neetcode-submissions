"""
Idea: the best case is it is an increasing series,
then we don't need to do anything.

So we use an extra monotonically decreasing stack to store those not aligned

e.g.
temps = [30,38,30,36,35,40,28]
[(40,5), (28,6) ]

Time: O(n)
Space: O(n)
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(temperatures[0],0)]
        res = [0]*len(temperatures)

        for i, t in enumerate(temperatures[1:], start=1):
            # compare w/ top until not larger
            while stack and stack[-1][0] < t:
                _, p_i = stack.pop()
                res[p_i] = i-p_i
            
            stack.append((t,i))
        
        return res
        









