# https://leetcode.com/problems/self-dividing-numbers/
class Solution:
    def numberFactors(self,n):
        a=list(str(n))
        lst=[]
        for i in a:
            if i!='0':
                lst.append(int(i))  
        return lst
    def selfDividingNumbers(self, left, right):
        res=[]
        for i in range(left,right+1):
            for k in self.numberFactors(i):
                if i% k!=0:
                    break
            else:
                res.append(i)
        return res
s=Solution()
print(s.numberFactors(20))


