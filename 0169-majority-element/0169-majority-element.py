class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = {}
        b = {}
        x = []
        
        for i in range(len(nums)):
                a[nums[i]] = a.get(nums[i], 0) + 1
        for val in a.values():
             x.append(val)
        for k,v in a.items():
            b[v] = k
        return b[max(x)]