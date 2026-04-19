# use a stack
# for Left ones, push them sequentially
# for right ones, check the top of the stack, if match, pop the top
# if not match or at the end stack is not empty, return F

# time: O(n)
# space: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {')':'(', '}':'{', ']':'['}
        for ch in s:
            # left ones: push
            if ch not in mp.keys(): 
                stack.append(ch)
                continue
            # right ones
            if stack and stack[-1] == mp[ch]: stack.pop() # match: pop
            else: return False
        
        return len(stack) == 0
            
        