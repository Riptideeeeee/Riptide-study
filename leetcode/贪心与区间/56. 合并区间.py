class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans=[intervals[0]]
        for left ,right in intervals:
            if left<=ans[-1][1]:
                ans[-1][1]=max(ans[-1][1],right)
            else:
                ans.append([left,right])
        return ans
      #将所给的数组按左边的数字排序，排序之后遍历，如果区间左开口小于上一个区间的右开口，那么就将存储的right更改为现在的区间的右开口，然后将这个区间存储进ans中
