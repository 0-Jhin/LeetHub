class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        m = list(t)
        for i in s:
            if i in m:
                m.remove(i)
            else:
                return False
        
        return True