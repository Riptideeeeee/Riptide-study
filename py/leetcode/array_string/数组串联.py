class Solution:
    def getConcatenation(self, nums):
        n=len(nums)
        new=[0]*2*n
        for i in range(0,n):
            new[i+n]=nums[i]
            new[i]=nums[i]
        return new