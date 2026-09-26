class Solution:
    def minimumTotal(self, triangle) -> int:
        n=len(triangle)
        cost = [[0] * (i + 1) for i in range(n)]
        for i in range(0,len(triangle)):
            for j in range(0,len(triangle[i])):
                if i==0 and j==0:
                    cost[i][j]=triangle[i][j]
                elif j==len(triangle[i])-1 and i!=0:
                    cost[i][j]=cost[i-1][j-1]+triangle[i][j]
                elif j==0 and i!=0:
                    cost[i][j]=cost[i-1][j]+triangle[i][j]
                else:
                    cost[i][j]=min(cost[i-1][j],cost[i-1][j-1])+triangle[i][j]
        return min(cost[-1])
        # for a in range(len(cost[i])):
        #     if a==0:
        #         m=cost[i][a]
        #     else:
        #         m = min(m, cost[i][a])
        #
        # return m
s=Solution()
print(s.minimumTotal([[-10]]))