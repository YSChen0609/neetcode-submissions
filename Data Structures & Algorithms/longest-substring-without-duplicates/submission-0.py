# idea start with 2, the ngradually increasing the "window"
# 1. l, r = 0, 1
# 2. if r+1 not having duplicates, keep moving
# 3. if duplicates, l+=1 until no duplicates
# 4. use a set to check duplicates

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # edge cases
        if len(s) <= 1: return len(s)

        # start with len(s)>=2 cases
        l, r = 0, 1
        res = 0
        visited = set([s[0]])
        # pwwkew
        # vis = {p, w}
        while l<len(s) and r<len(s):
            while s[r] in visited and l<=r-1:
                visited.remove(s[l])
                l += 1

            visited.add(s[r])
            res = max(res, r-l+1)
            r += 1

        return res

