class Solution(object):
    def groupAnagrams(self, strs):
        stdStrs = [''.join(sorted(std)) for std in strs]
        checkStr = list(set(stdStrs))
        reStrs = [[] for _ in range(len(checkStr))]
        for i in strs:
            key = ''.join(sorted(i))
            j = checkStr.index(key)
            reStrs[j].append(i)
        return reStrs