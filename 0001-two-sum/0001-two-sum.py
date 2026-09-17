class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = []
        i = 0
        req_num = 0
        n = len(nums)
        while i < n:
            req_num = target - nums[i]
            if req_num in nums[i+1:]:
                a.append(i)
                a.append(nums.index(req_num, i+1))
                return a
            i += 1