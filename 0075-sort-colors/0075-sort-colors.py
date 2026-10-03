class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        a = 0
        max_nums = max(nums)
        arr = [0] * (max_nums + 1)
        for i in nums:
            if arr[i] == 0:
                arr[i] = 1
            else:
                arr[i] += 1
        for x in range(len(arr)):
            for z in range(arr[x]):
                nums[a] = x
                a += 1