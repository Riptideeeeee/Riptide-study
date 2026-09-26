class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        lastnum=nums[0]
        maxnum=nums[0]
        for i in range(1,len(nums)):
            lastnum=max(nums[i],lastnum+nums[i])
            maxnum=max(maxnum,lastnum)
        return maxnum
#这里如果和上一个数相加变小，就丢掉，不然就加上
