class Solution(object):
    def reverseWords(self, s):
        rs = s.split()
        rs.reverse()
        return (" ".join(rs))