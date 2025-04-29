class Solution(object):
    def romanToInt(self, s):
        rs = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        r = 0
        for i in range(len(s)-1):
            if rs[s[i]] < rs[s[i+1]]:
                r -= rs[s[i]]
            else:
                r += rs[s[i]]
        r += rs[s[-1]]
        return r