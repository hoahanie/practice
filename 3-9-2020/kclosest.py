# https://leetcode.com/problems/k-closest-points-to-origin/
import math
class Solution:
    def kClosest(self, points, K):
        res=[]
        b=[]
        for i in points:
            res.append(math.sqrt((i[0])**2+(i[1])**2))
            b.append(math.sqrt((i[0])**2+(i[1])**2))
        b.sort()
        a=b[:K]
        result=[]
        for i in range(len(res)):
            if res[i] in a:
                print(res[i])
                result.append(points[i])  
        return result
s=Solution()
print(s.kClosest([[3,3],[5,-1],[-2,4]],2))
