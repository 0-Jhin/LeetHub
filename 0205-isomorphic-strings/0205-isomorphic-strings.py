class Solution(object):
    def isIsomorphic(self, s, t):
        ds = {}
        dt = {}
        for i in range(len(s)):
            if (s[i] in ds and t[i] != ds[s[i]]) or (t[i] in dt and s[i] != dt[t[i]]):
                return False
            ds[s[i]] = t[i]
            dt[t[i]] = s[i]
        return True