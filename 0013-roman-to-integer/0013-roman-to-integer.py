class Solution(object):
    def romanToInt(self, s):
        rs = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        r = 0
        pre = 0
        for i in reversed(s):
            if rs[i] < pre:
                r -= rs[i]
            else:
                r += rs[i]
                pre = rs[i]
            print(r, i, pre)
        return r