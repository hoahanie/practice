# https://leetcode.com/problems/di-string-match/

class Solution:
    def diStringMatch(self, S):
        n =len(S)
        a = list(range(0,n+1))
        res =[]
        for i in S:
            if i=='I':
                res.append(a.pop(0))
            else:
                res.append(a.pop())
        res.append(a.pop())
                
        return res
        
s=Solution()
print(s.diStringMatch("IDID"))
        