class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        # 动态规划数组
        num = [0] * (n + 1)
        num[1] = 1
        num[2] = 2
        for i in range(3, n + 1):
            num[i] = num[i-1] + num[i-2]
        return num[n]