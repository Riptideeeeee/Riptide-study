import marshal


class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        lines=[]
        crosses=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    crosses.append(i)
                    lines.append(j)
        lines=set(lines)
        crosses=set(crosses)
        for i in crosses:
            matrix[i]=[0]*len(matrix[0])
        for j in lines:
            for i in range(len(matrix)):
                matrix[i][j]=0
s = Solution()
s.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])