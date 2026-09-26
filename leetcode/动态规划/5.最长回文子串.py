class Solution:
    def longestPalindrome(self, s) -> str:
        cut=list(s)+['']
        maxlen=0
        place=0
        for i in range(len(cut)):
            #先判断奇数中心
            nowlen=0
            #判断是否是奇数中心
            for j in range(0,len(cut)):
                if i-j<0 or i+j>=len(cut):
                    #超出边界，退出循环
                    break
                elif cut[i+j]==cut[i-j]:
                    if j==0:
                        nowlen+=1
                        if maxlen<nowlen:
                            maxlen=nowlen
                            place=i
                    else:
                        nowlen+=2
                        #如果max小于现在的，修改max和place
                        if maxlen<nowlen:
                            maxlen=nowlen
                            place=i
                        else:
                            pass
                else:
                    break
            # 判断是否是偶数中心
            nowlen=0
            for j in range(0, len(cut)):
                if i - j < 0 or i + 1 + j >= len(cut):
                    # 超出边界，退出循环
                    break
                elif cut[i + 1 + j] == cut[i - j]:
                    nowlen += 2
                    # 如果max小于现在的，修改max和place
                    if maxlen < nowlen:
                        maxlen = nowlen
                        place = i
                    else:
                        pass
                else:
                    break
        output=''
        if maxlen % 2 == 0:
            for e in range(maxlen // 2):
                output = cut[place - e] + output + cut[place + 1 + e]
        elif maxlen % 2 == 1:
            for e in range((maxlen // 2)+1):
                if e==0:
                    output=cut[place - e]
                else:
                    output = cut[place - e] + output + cut[place + e]
        return output

s=Solution()
#abbcccba
#01234567
print(s.longestPalindrome("abbcccba"))



