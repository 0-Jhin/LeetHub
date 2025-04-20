class Solution(object):
    def summaryRanges(self, nums):
        summaryArr = []
        if len(nums) == 0 : return nums

        rangeStart = nums[0]
        rangeEnd = 0
        for i in range(1, len(nums)):
            if nums[i-1]+1 != nums[i]:
                rangeEnd = nums[i-1]
                if rangeStart == rangeEnd:
                    summaryArr.append(str(rangeStart))
                else:
                    numRange = "%d->%d" %(rangeStart, rangeEnd)
                    summaryArr.append(numRange)
                rangeStart = nums[i]
        rangeEnd = nums[len(nums)-1]
        if rangeStart == rangeEnd:
            summaryArr.append(str(rangeStart))
        else:
            numRange = "%d->%d" %(rangeStart, rangeEnd)
            summaryArr.append(numRange)
        return (summaryArr)