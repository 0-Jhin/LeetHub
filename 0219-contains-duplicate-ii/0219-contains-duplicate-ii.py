class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = set()

        for i in range(len(nums)):
            if nums[i] in seen:
                return True

            seen.add(nums[i])

            # 윈도우 크기 유지: k보다 크면 오래된 요소 제거
            if len(seen) > k:
                seen.remove(nums[i - k])

        return False