class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        a = {}
        n = len(nums)
        i = 0
        for i in range(n):
            req_num = target - nums[i]
            if req_num in a:
                return [a[req_num],i]
            a[nums[i]] = i