class Solution:
    def maximalSquare(self, matrix) -> int:
        y=len(matrix)
        x=len(matrix[0])
        length=min(y,x)
        maxS=0
        def judge(i, j):
            if matrix[j][i]=="1":
                return True
            else:
                return False
        def expand(i,j,a):
            for row in range(j, j+a+1):
                if matrix[row][i+a] != '1':
                    return False
            for col in range(i, i+a+1):
                if matrix[j+a][col] != '1':
                    return False
            return True
        for j in range(y):
            for i in range(x):
                if judge(i,j):
                    for a in range(0,length+1):
                        if i+a>=x or j+a>=y:
                            maxS = max(maxS,a * a)
                            break
                        elif expand(i,j,a):
                            maxS = max(maxS,  a* a)
                            pass
                        else:
                            maxS = max(maxS,  a* a)
                            break
                else:
                    pass
        return maxS

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
s = Solution()
print(s.maximalSquare(matrix))