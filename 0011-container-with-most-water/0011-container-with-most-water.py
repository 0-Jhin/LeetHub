class Solution(object):
    def maxArea(self, height):
        start = 0
        end = len(height)-1
        max_area = 0

        while start < end:
            h = min(height[start], height[end])
            w = end - start
            max_area = max(max_area, h * w)

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return max_area