class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = {}
        for i in range(len(nums)):
                a[nums[i]] = a.get(nums[i], 0) + 1
                if a[nums[i]] > len(nums)//2:
                    variable = nums[i]
                    return variable        