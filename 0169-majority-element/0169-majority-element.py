class Solution(object):
    def majorityElement(self, nums):
        k = list(set(nums))
        l = []
        for i in k:
            l.append(nums.count(i))
        return (k[l.index(max(l))])
