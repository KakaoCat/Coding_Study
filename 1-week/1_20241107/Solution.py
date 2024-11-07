class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        counter = collections.Counter(nums) 
        sorted_nums, _ = zip(*sorted(counter.items(), key=lambda k:k[1], reverse = True)) 
        return sorted_nums[:k]
