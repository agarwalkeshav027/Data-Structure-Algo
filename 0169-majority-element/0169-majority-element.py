class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = {}
        max_num = 0
        for i in range(len(nums)):
                a[nums[i]] = a.get(nums[i], 0) + 1
                if a[nums[i]] > max_num:
                    max_num = a[nums[i]]
                    variable = nums[i]
        return variable