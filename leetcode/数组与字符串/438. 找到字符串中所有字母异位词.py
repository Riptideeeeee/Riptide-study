#这道题用时7700ms

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p=''.join(sorted(list(p)))
        m,n=len(s),len(p)
        ans=[]
        for i in range(m-n+1):
            now=''.join(sorted(list(s[i:i+n])))
            if now==p:
                ans.append(i)
        return ans
