class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if(m==0):
            nums1[:] = nums2[:]
        else:
            nums1[:] = nums1[:m]
            nums1.extend(nums2)
            nums1.sort()