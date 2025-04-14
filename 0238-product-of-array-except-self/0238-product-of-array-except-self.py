class Solution(object):
    def productExceptSelf(self, nums):
        multi = 1
        arr=[]
        
        for i in nums:
            arr.append(multi)
            multi *= i
        
        multi = 1

        for i in range(len(nums)-1, -1, -1):
            arr[i] *= multi
            multi *= nums[i]
    
        return arr
