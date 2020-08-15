# https://leetcode.com/problems/count-square-submatrices-with-all-ones/
class Solution:
    def printMaxtrix(self,matrix):
        for i in matrix:
            print(i)

    def countSquares(self, matrix):
        if len(matrix)==0:
            return 0
        dem = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
               if matrix[i][j]==1: dem += 1
        m = len(matrix)
        n = len(matrix[0])
        for k in range(1,min(m,n)):
            newMatrix = []
            for i in range(m-k):
                newMatrix.append([])
                for j in range(n-k):
                    if matrix[i][j] == 1:
                        if matrix[i][j+1] == 1 and matrix[i+1][j] == 1 and matrix[i+1][j+1] == 1:
                            newMatrix[i].append(1)
                            dem+=1
                        else:
                            newMatrix[i].append(0)
                    else:
                        newMatrix[i].append(0)
            matrix = newMatrix
        return dem
s=Solution()
print(s.countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]]))
    