# 1. get the (chr) freq of each str in strs: O(1000*100)
# 2. group strs with same freq using dict: {freq: [strs]}: O(1000)

from collections import defaultdict

class Solution:
    def get_freq(self, s: str) -> str:
        freq_str = [0] * 26
        for c in s: freq_str[ord(c)-ord('a')] += 1

        return str(freq_str)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            f_s = self.get_freq(s)
            groups[f_s].append(s)
        
        ans = []
        for g in groups.values(): ans.append(g)

        return ans
