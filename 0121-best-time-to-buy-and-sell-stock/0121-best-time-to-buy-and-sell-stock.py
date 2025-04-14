class Solution(object):
    def maxProfit(self, prices):
        pmin = prices[0]
        pmax = 0

        for i in prices:
            if i < pmin:
                pmin = i
            elif i - pmin > pmax:
                pmax = i - pmin
        return pmax