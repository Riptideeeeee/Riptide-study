class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        ways=[[0]*n]*m
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    ways[i][j]=0
                else:
                    if i == 0 and j == 0:
                        ways[i][j] = 1
                    elif i == 0 and j != 0:
                        ways[i][j] = ways[i][j - 1]
                    elif i != 0 and j == 0:
                        ways[i][j] = ways[i - 1][j]
                    elif i != 0 and j != 0:
                        ways[i][j] = ways[i - 1][j] + ways[i][j - 1]
        return ways[m-1][n-1]
s=Solution()
print(s.uniquePathsWithObstacles([[0,1],[0,0]]))


