class Solution:
    def deleteAndEarn(self, nums):
        m=0
        for i in range(len(nums)):
            m=max(m,nums[i])
        test=[0]*(m+1)
        for i in range(len(nums)):
            test[nums[i]]+=nums[i]
        if len(test)==1:
            return 0
        elif len(test)==2:
            return test[1]
        elif len(test)==3:
            return max(test[2],test[1])
        elif len(test)>=4:
            point=[0]*len(test)
            point[0]=0
            point[1]=test[1]
            point[2]=test[2]
            for i in range(3,len(test)):
                point[i]=test[i]+max(point[i-3],point[i-2])
            return max(point[i],point[i-1])
# 
# s=Solution()
# print(s.deleteAndEarn([1,1,1,1,1,1,1,1,1,1,1,1,2]))