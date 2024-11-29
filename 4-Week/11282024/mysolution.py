class Solution:
    def findMin(self, nums: List[int]) -> int: 

        left = 0; right = len(nums)-1

        while left<right:
            mid = (right+left)//2
            print(mid)
            if nums[mid]<nums[-1]:
                right = mid-1
            elif nums[mid]>nums[-1]:
                left = mid +1

            if nums[mid]>nums[mid+1]:
                return nums[mid+1]

            if nums[mid]<nums[mid-1]:
                return nums[mid] ## to consider [3,1,2] case.
            '''
            my initial code did not work at [3,1,2] case due to:
                
            if nums[mid]>nums[mid+1] and nums[mid]>nums[mid-1]:
                return nums[mid+1]
            '''

        return nums[0]
