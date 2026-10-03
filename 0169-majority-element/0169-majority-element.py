class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = {}
        arr = sorted(set(nums))
        arr = arr[::-1]
        times = len(nums)//2

        for i in range(len(nums)):
                a[nums[i]] = a.get(nums[i], 0) + 1
        for x in arr:
            max_num = x
            if a[max_num] > times:
                return max_num
     