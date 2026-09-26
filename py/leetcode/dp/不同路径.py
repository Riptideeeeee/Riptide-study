class Solution:
    def uniquePaths(self, m, n):
        ways=[[1]*(n)]*m
        for i in range(0,m):
            for j in range(0,n):
                if i==0 and j==0:
                    ways[i][j]=1
                elif i==0 and j!=0:
                    ways[i][j]=ways[i][j-1]
                elif j==0 and i!=0:
                    ways[i][j]=ways[i-1][j]
                elif i!=0 and j!=0:
                    ways[i][j]=ways[i][j-1]+ways[i-1][j]
        return ways[m-1][n-1]


