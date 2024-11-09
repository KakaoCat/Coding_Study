class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: 
        for start in nums:
            if start - 1 not in nums:
                end = start + 1
                while end in nums:
                    end +=1
                
                if end - start > long_seq:
                    long_seq = end-start
        return long_seq

