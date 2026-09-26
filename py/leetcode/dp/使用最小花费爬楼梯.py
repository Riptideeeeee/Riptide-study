
class Solution:
    def minCostClimbingStairs(self, cost):
        """从0阶开始"""
        all_cost=[0]*(len(cost)+1)
        if len(cost)==1 or len(cost)==2:
            return min(cost[0],cost[1])
        elif 2<len(cost):
            all_cost=[0]*(len(cost)+1)
            all_cost[0]=cost[0]
            all_cost[1]=cost[1]
            for i in range(2, len(cost)):
                all_cost[i] = cost[i] + min(all_cost[i - 2],all_cost[i - 1])
            return min(all_cost[len(cost)-1],all_cost[len(cost)-2])
