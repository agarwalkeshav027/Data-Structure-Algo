class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a={}
        x = []
        for i in range(len(nums)):
                a[nums[i]] = a.get(nums[i], 0) + 1
        for val in a.values():
             x.append(val)
        for k,v in a.items():
             if v == max(x):
                  return k