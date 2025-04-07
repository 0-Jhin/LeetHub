class Solution(object):
    def isPalindrome(self, s):
        pal = ""
        for i in s:
            if(i.isalpha() or i.isdigit()):
                pal+=i.lower()
        
        for i in range(len(pal)//2):
            if(pal[i] != pal[-i-1]):
                return False
        return True
        