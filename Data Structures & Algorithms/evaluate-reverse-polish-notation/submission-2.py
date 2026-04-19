# use a stack, push from start of the tokens list
# pop the operands when ever we encounter an operator
# cal the result and push it back to the stack, and go on
# time: O(n)
# space: O(n)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            # print(f'stack:{stack}')
            # operators encountered
            if t in ('+', '-', '*', '/'):
                y = stack.pop()
                x = stack.pop()
                if t == '+': stack.append(x+y)
                if t == '-': stack.append(x-y)
                if t == '*': stack.append(x*y)
                if t == '/': stack.append(int(x/y))
            else: stack.append(int(t))
        
        return stack[-1]
