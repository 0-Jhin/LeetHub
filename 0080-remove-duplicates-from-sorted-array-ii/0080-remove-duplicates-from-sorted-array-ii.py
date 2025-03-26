class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nS = list(set(nums))
        for i in nS:
            nC = nums.count(i)
            nI = nums.index(i)
            if(nC>2):
                del nums[nI+2 : nI+nC]
        k = len(nums)
        return k