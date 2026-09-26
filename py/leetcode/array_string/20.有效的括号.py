class Solution:
    def isValid(self, s: str) -> bool:
        dic={"(":0,
             "[":0,
             "{":0}
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]]+=1
            elif s[i]==")":
                if s[i-1]=="(":
                    dic["("] -= 1
                else:
                    return False
            elif s[i]=="]":
                if s[i-1]=="[":
                    dic["["] -= 1
                else:
                    return False
            elif s[i]=="}":
                if s[i-1]=="{":
                    dic["{"] -= 1
                else:
                    return False
        if dic=={"(":0,"[":0,"{":0}:
            return True
        else:
            return False