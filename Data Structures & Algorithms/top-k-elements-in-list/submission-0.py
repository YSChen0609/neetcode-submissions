# use a max heap
# 1. loop the nums list, get the freq list [[n, freq]]
# 2. heapify the freq list (sorted is fine)
# 3. take the last 3 
# time: O(nlogn)
# space: O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. get the freq
        freq = {}
        for n in nums: freq[n] = freq.get(n, 0) + 1
        # 2. sort the freq
        freq = [[n,f] for n, f in freq.items()]
        freq = sorted(freq, key=lambda x: -x[1])
        # 3. take the first 3
        return [x[0] for x in freq[:k]]

