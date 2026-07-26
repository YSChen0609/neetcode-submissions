"""
Use sliding window + hashmap to trace chr freq within the window

ptrs start from the left most, gradually move R until the window is not Valid, then move L until it is once again.
This will scan thru all possible combination efficiently

Time: O(n*26)-26 for finding the max freq chr
Space: O(26) for the hashmap
"""

"""
s = "AAABABB", k = 1
l, r = 0, 0
res = 
freq = {A: 4, B:2}
"""
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        res = 0
        l, r = 0, 0
        freq[s[l]] += 1 
        
        while r<len(s) and l<=r:
            # check if current window is valid
            print(s[l:r+1])
            win_size = r-l+1
            if win_size - max(freq.values()) <= k:
                res = max(res, win_size)
                r += 1
                if r<len(s):
                    freq[s[r]] += 1
            else:
                freq[s[l]] -= 1
                l += 1
                
            
        return res
            
            








