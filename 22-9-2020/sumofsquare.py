import math
class Solution:
    def judgeSquareSum(self, c):
        a=int( math.sqrt(c))
        while a >0:
            if math.sqrt(c-a**2)==int(math.sqrt(c-a**2)):
                return True
            a-=1
        return False

s=Solution()
print(s.judgeSquareSum(7))
