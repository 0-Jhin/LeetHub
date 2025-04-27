class Solution(object):
    def wordPattern(self, pattern, s):
        ss = s.split(" ")
        if len(pattern) != len(ss):
            return False
        ds = {}
        dt = {}
        for i in range(len(pattern)):
            if (ss[i] in ds and pattern[i] != ds[ss[i]]) or (pattern[i] in dt and ss[i] != dt[pattern[i]]):
                return False
            ds[ss[i]] = pattern[i]
            dt[pattern[i]] = ss[i]
        return True
        