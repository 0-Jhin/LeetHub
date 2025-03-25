class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nS = list(set(nums))
        for i in nS:
            if(nums.count(i)>2):
                for j in range((nums.count(i)-2)):
                    nums.remove(i)
        k = len(nums)
        return k