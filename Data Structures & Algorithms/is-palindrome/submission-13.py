# use two-ptr
# l forward, r backward
# if s[l] != s[r], return F, until they meet

# time: O(n)
# space: O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        if l == r: return True
        while l <= r:
            # skip non-alnum. and spaces
            if not s[l].isalnum() or (s[l] == ' '): 
                l += 1
                continue
            if not s[r].isalnum() or (s[r] == ' '): 
                r -= 1
                continue
            # check cond.
            if s[l].lower() != s[r].lower(): return False
            # update the ptrs
            l += 1
            r -= 1
            
        
        return True