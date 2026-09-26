class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        请勿返回任何内容，而是就地修改 nums。
        """
        for i in range(k):
            x=nums.pop()
            nums.insert(0,x)
