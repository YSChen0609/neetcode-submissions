# maintain a stack (val small to large), w/ (val, idx)
# To push a new item, comp. it with the top, if larger than the top, pop the origin top(s) 
# until no-larger, then push the new item

# time: O(2n)
# space: O(n)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #(val, idx)
        res = [0] * len(temperatures)
        
        for i, temp in enumerate(temperatures):
            # comp. top w/ new item
            while stack and temp > stack[-1][0]: # pop top(s) until can't
                top = stack.pop(-1)
                res[top[1]] = i-top[1]
            stack.append((temp,i))
        
        return res


