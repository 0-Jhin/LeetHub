class Solution(object):
    def isSubsequence(self, s, t):
        tex = list(t)
        for i in s:
            if(i in tex):
                tex = tex[tex.index(i):]
                tex.remove(i)
            else:
                return False
        return True
        