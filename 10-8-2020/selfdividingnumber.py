# https://leetcode.com/problems/self-dividing-numbers/
class Solution:
    def numberFactors(self,n):
        a=list(str(n))
        lst=[]
        for i in a:
            lst.append(int(i))  
        return lst
    def selfDividingNumbers(self, left, right):
        res=[]
        for i in range(left,right+1):
            if 0 not in self.numberFactors(i):
                check =True
                for k in self.numberFactors(i):
                    if i% k!=0:
                        check =False
                        break
                if check ==True:
                    res.append(i)
        return res
s=Solution()
print(s.selfDividingNumbers(1,25))



