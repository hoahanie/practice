# https://leetcode.com/problems/count-square-submatrices-with-all-ones/
class Solution:
    def checkMaxtrix(self, ax, ay, bx, by, matrix):
        for i in range(ax,bx+1):
            for j in range(ay,by+1):
                if matrix[i][j]==0:
                    return False
        return True

    def countSquares(self, matrix):
        if len(matrix)==0:
            return 0

        else:
            dem=0
            for i in matrix:
                for j in i:
                    if j ==1:
                        dem+=1
            print(dem)
            n=min(len(matrix),len(matrix[0]))
            for h in range(2,n+1):
                if h==2:
                    for j in range(0,len(matrix[0])-1):
                        for i in range(0,len(matrix)-1):
                            if matrix[i][j]==1 and matrix[i][j+1]==1 and matrix[i+1][j]==1 and matrix[i+1][j+1]==1:
                                dem+=1    
                print(dem)
                if h>2:
                    for k in range(2,h):
                        for i in range(0,len(matrix[0])-k):
                            for j in range(0,len(matrix)-k):
                                if self.checkMaxtrix(i,j,i+k,j+k,matrix):
                                    dem+=1
        return dem
s=Solution()
print(s.countSquares([[1,1,0,0,1],[1,0,1,1,1],[1,1,1,1,1],[1,0,1,0,1],[0,0,1,0,1]]))
    