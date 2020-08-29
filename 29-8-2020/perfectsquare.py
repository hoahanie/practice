# https://leetcode.com/problems/perfect-squares/
import math
class Solution:
    def numSquares(self, n):
        f= [0]*(n+1)
        g=[]
        for i in range(1,n+1):
            if (int(math.sqrt(i)))**2== i:
                f[i]=1
                g.append(i)
            else:
                for j in g:
                    if f[i]==0:
                        f[i]=f[j]+f[i-j]
                    else:
                        f[i]=min(f[i],f[j]+f[i-j])
        return f[n]
s=Solution()
print(s.numSquares(13))
        