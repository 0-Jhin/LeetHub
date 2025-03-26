class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        L = len(nums)
        if(L<k):
            nL = L-k%L
        else:
            nL = L-k
        nums2 = nums[:nL]
        del nums[:nL]
        nums.extend(nums2)

        
        