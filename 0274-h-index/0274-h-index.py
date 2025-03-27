class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        L = len(citations)
        for i in range(L):
            if citations[i] >= L - i:
                return L - i
        return 0