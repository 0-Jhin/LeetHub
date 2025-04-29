class Solution(object):
    def intToRoman(self, num):
        num_roman = {0: '', 1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        rs = ""
        for i in range(4):
            d = 1000 // 10**i
            n = num // d
            if n == 9:
                rs += num_roman[d] + num_roman[d * 10]
                num -= d * 9
            elif n > 4:
                rs += num_roman[d * 5]
                rs += num_roman[d] * (n-5)
                num -= d * n
            elif n == 4:
                rs += num_roman[d] + num_roman[d * 5]
                num -= d * 4
            else:
                rs += num_roman[d] * n
                num -= d * n
            print(rs)
        return rs