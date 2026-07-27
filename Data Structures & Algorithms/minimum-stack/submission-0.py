"""
The hard point is "how do we know the Min after it pops"
Solution: use a seperate stack to store the "min so far" for "each top"
"""

class MinStack:

    def __init__(self):
        self.stack = [] #element=[val, min_so_far]

    def push(self, val: int) -> None:
        if self.stack:
            min_so_far = min(val, self.stack[-1][1])
        else: min_so_far = val

        self.stack.append([val, min_so_far])

    def pop(self) -> None:
        self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
