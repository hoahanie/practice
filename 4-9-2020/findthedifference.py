# https://leetcode.com/problems/find-the-difference/
class Solution:
    def findTheDifference(self, s,t):
        d=dict()
        d1=dict()
        for i in s:
            d[i]=d.get(i,0)+1
        for i in t:
            d1[i]=d1.get(i,0)+1
        for i in d1:
            if i not in d:
                return i
            elif i in d and d1[i]>d[i]:
                return i*(d1[i]-d[i])
s=Solution()
print(s.findTheDifference("abcd","abcde"))