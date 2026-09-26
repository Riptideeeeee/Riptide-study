class Solution:
    def minPathSum(self, grid) -> int:
        cost=[[0]*len(grid[0])]*len(grid)
        cost[0][0]=grid[0][0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i==0 and j==0:
                    cost[i][j]=grid[i][j]
                elif i==0 and j!=0:
                    cost[i][j]=cost[i][j-1]+grid[i][j]
                elif i!=0 and j==0:
                    cost[i][j]=cost[i-1][j]+grid[i][j]
                elif i!=0 and j!=0:
                    cost[i][j]=min(cost[i-1][j],cost[i][j-1])+grid[i][j]
                # print(f"{i}  {j}  {cost[i][j]}")
        return cost[i][j]
