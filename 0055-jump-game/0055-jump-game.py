class Solution(object):
    def canJump(self, nums):
        reach = 0
        for i in range(len(nums)):
            if i > reach:
                return False  # 현재 위치 i에 도달할 수 없으면 실패
            reach = max(reach, i + nums[i])  # 최대 도달 인덱스 갱신
        return True
