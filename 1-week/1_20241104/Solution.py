class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool: 
        hashmap = dict()
        for n in nums:
            if hashmap.get(n, None)== None:
                hashmap[n] = 1
            else:
                return True
        return False 
