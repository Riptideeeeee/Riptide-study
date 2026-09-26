class Solution:
    def maximalSquare(self, matrix) -> int:
        x=len(matrix[0])
        y=len(matrix)
        maxsize=0
        dp=[[0 for _ in range(x+1)] for _ in range(y+1)]
        for i in range(1,y+1):
            for j in range(1,x+1):
                if matrix[i-1][j-1]=="1":
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                    maxsize=max(maxsize,dp[i][j])
                print(dp,"\n")
        return maxsize*maxsize