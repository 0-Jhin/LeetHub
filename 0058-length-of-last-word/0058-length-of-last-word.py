class Solution(object):
    def lengthOfLastWord(self, s):

        ls = s.strip().split(" ")
        return len(ls[-1])
        