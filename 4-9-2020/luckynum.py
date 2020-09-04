# https://leetcode.com/problems/find-lucky-integer-in-an-array/
class Solution:
    def findLucky(self, arr):
        d=dict()
        for i in arr:
            d[i]=d.get(i,0)+1
        res=[]
        for i in d:
            if i==d[i]:
                res.append(i)
        if res==[]:
            return -1 
        else:
            return max(res)
s=Solution()
print(s.findLucky([1,2,2,3,3,3]))