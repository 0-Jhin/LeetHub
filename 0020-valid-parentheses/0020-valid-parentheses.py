class Solution(object):
    def isValid(self, s):
        if len(s) < 2:
            return False
        openBraket = ['(', '{', '[']
        closeBraket = [')', '}', ']']
        braket = []
        for i in s:
            if(i in openBraket):
                braket.append(i)
            elif i in closeBraket:
                if braket == []:
                    return False
                if braket.pop() != openBraket[closeBraket.index(i)]:
                    return False
        if braket == []:
            return True
        else:
            return False