class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums1 = set(nums)
        for i in nums1:
            if nums.count(i) > len(nums)/2:
                return (i)
                
            

                
        