class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        m = list(magazine)
        for i in ransomNote:
            if i in m:
                m.remove(i)
            else:
                return False
        return True