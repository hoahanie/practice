# https://leetcode.com/problems/perfect-number/
import math
class Solution:
    def findPositiveDivisor(self,n):

        res = [1]
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                res.append(n//i)
                res.append(i)
        print(res)
        return res
    def checkPerfectNumber(self, num):
        if n<=1: return False
        else:
            if num==sum(self.findPositiveDivisor(num)):
                return True
            return False
s=Solution()
print(s.checkPerfectNumber(45))
