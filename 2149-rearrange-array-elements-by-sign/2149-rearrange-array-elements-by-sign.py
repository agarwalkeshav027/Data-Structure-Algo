class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        positive = []
        negative = []
        rearrangearr = []
        for i in nums:
            if i < 0:
                negative.append(i)

            else:
                positive.append(i)
        final = list(zip(positive,negative))
        for pair in final:
            for item in pair:
                rearrangearr.append(item)
        

        return rearrangearr