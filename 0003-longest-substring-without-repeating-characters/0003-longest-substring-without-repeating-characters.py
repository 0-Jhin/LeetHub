class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            if s[right] in char_index and char_index[s[right]] >= left:
                # 중복 문자 발견 시 left 갱신
                left = char_index[s[right]] + 1

            # 현재 문자의 인덱스 저장 (또는 갱신)
            char_index[s[right]] = right

            # 최대 길이 갱신
            max_length = max(max_length, right - left + 1)

        return max_length