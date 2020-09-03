# https://leetcode.com/problems/custom-sort-string/
class Solution:
    def customSortString(self, S,T):
        a=list(S)
        b=list(T)
        res= []
        for i in a:
            while i in b:
                res.append(i)
                b.remove(i)
        t = "".join(res+b)
        print(res)
        print(b)
        return t
s=Solution()
print(s.customSortString ("kqep","pekeq"))
            
