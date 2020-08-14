# https://leetcode.com/problems/count-square-submatrices-with-all-ones/
class Solution:
    def countSquares(self, matrix):
        if len(matrix)==0:
            return 0

        else:
            dem=0
            for i in matrix:
                for j in i:
                    if j ==1:
                        dem+=1
            n=min(len(matrix),len(matrix[0]))
            for k in range(1,n):
                for j in range(0,len(matrix[0])-k):
                    for i in range(0,len(matrix)-k):
                        if matrix[i][j]==1 and matrix[i][j+k]==1 and matrix[i+k][j]==1 and matrix[i+k][j+k]==1:
                            dem+=1

        return dem
s=Solution()
print(s.countSquares([
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]))
    