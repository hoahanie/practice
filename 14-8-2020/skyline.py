import numpy as np
class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        sumGridOri=0
        for i in grid:
            for j in i:
                sumGridOri+=j
        lr=[]
        for i in grid:
            lr.append(max(i))
        tb=[]
        for i in np.transpose(grid):
            tb.append(max(i))
        for i in range(0,len(lr)):
            for j in range(0,len(tb)):
                grid[i][j]=min(lr[i],tb[j])
        sumGridTrans=0
        for i in grid: 
            for j in i: 
                sumGridTrans+=j
        n =sumGridTrans-sumGridOri
        return n

s=Solution()
print(s.maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))
