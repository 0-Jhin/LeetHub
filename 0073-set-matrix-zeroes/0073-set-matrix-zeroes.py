class Solution(object):
    def setZeroes(self, matrix):
        
        m = len(matrix)
        n = len(matrix[0])
        arr=[]

        for i in range(m):
            if 0 in matrix[i]:
                for j in range(n):
                    if(matrix[i][j] == 0):
                        arr.append(j)
                    matrix[i][j] = 0
        for i in range(m):
            for j in arr:
                matrix[i][j] = 0
