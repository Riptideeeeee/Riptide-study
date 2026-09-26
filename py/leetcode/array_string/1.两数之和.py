class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j:
                    continue
                elif nums[i]+nums[j] == target:
                    return [i, j]

# class Solution:
#     def twoSum(self, nums, target):
#         for i in range(len(nums)):
#             complement = target - nums[i]
#             if nums.count(complement)==1 and complement==nums[i]:
#                 continue
#             else:
#                 if complement in nums:
#                     return [i,nums.index(complement)]

s = Solution()
print(s.twoSum([3,3,1,4], 6))
