class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i in range(len(nums)-1):
            if nums[i+1] == nums[i]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)