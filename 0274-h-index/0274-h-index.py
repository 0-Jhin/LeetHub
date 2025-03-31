class Solution(object):
    def hIndex(self, citations):
        citations.sort()
        L = len(citations)
        for i in range(L):
            if citations[i] >= L - i:
                return L - i
        return 0