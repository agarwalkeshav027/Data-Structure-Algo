class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = []
        total = 0
        for i in range(len(nums)):
            a = []
            if target >= nums[i] or target <= nums[i]:
                total = nums[i]
                a.append(i)
            for j in range(i+1, len(nums)):
                if total + nums[j] == target:
                    a.append(j)
                    return a 