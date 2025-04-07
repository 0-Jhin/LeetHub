class Solution(object):
    def twoSum(self, numbers, target):
        start = 0
        end = len(numbers) - 1
        while start < end:
            if numbers[start] + numbers[end] == target:
                break
            elif numbers[start] + numbers[end] > target:
                end -= 1
            else:
                start += 1
        return [start + 1, end + 1]