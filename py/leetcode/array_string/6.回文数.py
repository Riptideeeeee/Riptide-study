class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=list(str(x))
        for i in range(len(n)//2):
            if n[i]==n[len(n)-i-1]:
                continue
            else:
                return False
        return True