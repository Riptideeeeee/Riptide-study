class Solution:
    def tranintodict(self,s):
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        return dic
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cut=self.tranintodict(ransomNote)
        dic=self.tranintodict(magazine)
        for i in cut:
            if i in dic:
                if dic[i]>=cut[i]:
                    continue
                else:
                    return False
            else:
                return False
        return True
# s = Solution()
# print(s.canConstruct(ransomNote="abdd", magazine="baada"))
