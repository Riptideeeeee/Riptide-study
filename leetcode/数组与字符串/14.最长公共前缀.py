class Solution:
    def longestCommonPrefix(self, strs) -> str:
        ans=""
        for i in range(len(strs[0])):
            for str in strs:
                if len(str)<i+1:
                    return ans
                else:
                    if str[i] != strs[0][i]:
                        return ans
                    elif str[i] == strs[0][i]:
                        pass
            ans=ans+strs[0][i]
        return ans
# s = Solution()
# print(s.longestCommonPrefix(["abcabc","abc","abc"]))

