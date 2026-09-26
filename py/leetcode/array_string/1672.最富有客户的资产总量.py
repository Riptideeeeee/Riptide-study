class Solution:
    def maximumWealth(self, accounts) -> int:
        wealth=[0]*len(accounts)
        maxWealth=0
        for i in range(0,len(accounts)):
            for j in range(0,len(accounts[i])):
                wealth[i]+=accounts[i][j]
            if wealth[i]>maxWealth:
                maxWealth=wealth[i]
        return maxWealth
# s=Solution()
# print(s.maximumWealth([[1,2,3],[3,2,1]]))
