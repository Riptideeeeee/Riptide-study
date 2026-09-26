class Solution:
    def romanToInt(self, s: str) -> int:
        n=list(s)
        num=0
        for i in range(len(n)):
            if n[i]=='I':
                num+=1
            if n[i]=='V':
                if n[i-1]=='I' and i!=0:
                    num+=3
                else:
                    num+=5
            if n[i]=='X':
                if n[i-1]=='I' and i!=0:
                    num+=8
                else:
                    num+=10
            if n[i]=='L':
                if n[i-1]=='X' and i!=0:
                    num+=30
                else:
                    num+=50
            if n[i]=='C':
                if n[i-1]=='X' and i!=0:
                    num+=80
                else:
                    num+=100
            if n[i]=='D':
                if n[i-1]=='C' and i!=0:
                    num+=300
                else:
                    num+=500
            if n[i]=='M':
                if n[i-1]=='C' and i!=0:
                    num+=800
                else:
                    num+=1000
        return num
# s = Solution()
# print(s.romanToInt("CDLXIX"))