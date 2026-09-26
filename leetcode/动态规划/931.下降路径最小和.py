class Solution:
    def minFallingPathSum(self, matrix) -> int:
        cost=[[float('inf')]*(len(matrix[0])+2) for _ in range(len(matrix))]
        cost[0]=[float('inf')]+matrix[0]+[float('inf')]
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])+1):
                cost[i][j]=min(cost[i-1][j],cost[i-1][j-1],cost[i-1][j+1])+matrix[i][j-1]
                print(cost)
        return min(cost[-1])
matrix = [[2,1,3],[6,5,4],[7,8,9]]
s=Solution()
print(s.minFallingPathSum(matrix))
