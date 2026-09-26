# class Solution:
#     def runningSum(self, nums):
#         result=nums[:]
#         for i in range(0,len(nums)):
#             for j in range(i+1,len(nums)):
#                 result[j]+=nums[i]
#         return result

class Solution:
    def runningSum(self, nums):
        result=nums[:]
        for i in range(1,len(nums)):
            result[i]=result[i]+result[i-1]
        return result

s=Solution()
print(s.runningSum([1,2,3,4]))
