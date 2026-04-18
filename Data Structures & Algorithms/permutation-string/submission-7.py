# 1. check which one is longer
# 2. for the shorter one, create a window (2-ptrs) same size of it
# 3. slide the window in the longer one
# for each iteration, check if the count of the lower cases are the same (using dict)

# time: O(s2)
# space: O(1)


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # check s2 is the longer one
        l1, l2 = len(s1), len(s2) # alias
        if l1 > l2: return False
        # get s1-chr-cnt
        s1_chrs = [0] * 26 # const
        for c in s1: s1_chrs[ord(c)-ord('a')] += 1

        # init s2-chr-cnt 
        s2_chrs = [0] * 26
        for i in range(0, l1): s2_chrs[ord(s2[i])-ord('a')] += 1

        if s1_chrs == s2_chrs: return True

        # start sliding
        for i in range(l1, l2):
            s2_chrs[ord(s2[i])-ord('a')] += 1
            s2_chrs[ord(s2[i-l1])-ord('a')] -= 1
            if s1_chrs == s2_chrs: return True
        
        return False



