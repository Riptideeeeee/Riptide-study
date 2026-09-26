class Solution:
    def wordBreak(self, s, wordDict) -> bool:
        n=len(s)
        dp=[True]+[False]*(n)
        for i in range(0,n+1):
            for j in range(0,i+1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i]=True
                    break
        if dp[n]:
            return True
        else:
            return False

