class Solution(object):
    def isPalindrome(self, x):
        xs = str(x)
        if  x < 0:
            return False
        for i in range(len(xs)):
            if xs[i] != xs[-1-i]:
                return False
        return True
        