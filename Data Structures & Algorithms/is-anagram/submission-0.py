# use dict {chr: cnt}
# trav s, build the cnts, then de-cnt by trav t
# if there is any non-0s, return False
# time: O(S+T+26)
# space: O(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chrs = {}
        # cnt up from s
        for c in s: chrs[c] = chrs.get(c, 0) + 1
        # cnt down from t
        for c in t: chrs[c] = chrs.get(c, 0) - 1
        # check all zeros
        for c, cnt in chrs.items():
            if cnt != 0: return False
        # all zeros, is anagram
        return True
