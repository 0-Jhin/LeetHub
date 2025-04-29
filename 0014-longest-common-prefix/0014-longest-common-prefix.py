class Solution(object):
    def longestCommonPrefix(self, strs):
        rs = ""
        strs.sort()
        min_str = len(min(strs, key=len))
        for i in range(min_str):
            if strs[0][i] != strs[-1][i]:
                return rs
            else:
                rs += strs[0][i]
        return rs