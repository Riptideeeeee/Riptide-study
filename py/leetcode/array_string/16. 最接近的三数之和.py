class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        maxsum=0
        nums.sort()
        close_num=float('inf')
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            while left<right:
                if nums[left]+nums[right]+nums[i]>target:
                    if close_num>abs(nums[left]+nums[right]+nums[i]-target):
                        close_num=abs(nums[left]+nums[right]+nums[i]-target)
                        maxsum=nums[left]+nums[right]+nums[i]
                    right-=1
                elif nums[left]+nums[right]+nums[i]<target:
                    if close_num>abs(nums[left]+nums[right]+nums[i]-target):
                        close_num=abs(nums[left]+nums[right]+nums[i]-target)
                        maxsum=nums[left]+nums[right]+nums[i]
                    left+=1
                else:
                    maxsum=nums[left]+nums[right]+nums[i]
                    return maxsum
        return maxsum