#[2,7,9,3,1,8,6]
class Solution:
    def rob(self, nums):
        if len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return max(nums[0],nums[1])
        elif len(nums)==3:
            return max(nums[0]+nums[2],nums[1])
        elif len(nums)>=4:
            money=[0]*len(nums)
            money[0]=nums[0]
            money[1]=nums[1]
            money[2]=nums[2]+nums[0]
            for i in range(3,len(nums)):
                money[i]=nums[i]+max(money[i-3],money[i-2])
            return max(money[i],money[i-1])

s=Solution()
print(s.rob([2,7,9,3,1,8,6]))

test_cases = [
    ([1, 2, 3, 1], 4),
    ([2, 7, 9, 3, 1], 12),
    ([2, 1, 1, 2], 4),
    ([1, 3, 1, 3, 100], 103),
    ([1, 2, 3, 4, 5], 9),
    ([6, 1, 1, 6], 12),
    ([0], 0),
    ([5], 5),
    ([1, 2], 2),
    ([0, 0, 0, 0], 0),
]

for i, (nums, expected) in enumerate(test_cases, 1):
    result = s.rob(nums)
    print(f"测试 {i}: nums={nums} => 结果={result}, {'✅ 通过' if result == expected else '❌ 失败 (预期' + str(expected) + ')'}")

