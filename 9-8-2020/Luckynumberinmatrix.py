# https://leetcode.com/problems/lucky-numbers-in-a-matrix/
# import numpy
class Solution:
    def luckyNumbers (self, matrix):
        # newMatrix=numpy.transpose(matrix)
        newMatrix =[]
        lst=[]
        for k in range(0,len(matrix[0])):
            subMatrix=[]
            for i in range(0,len(matrix)):
                subMatrix.append(matrix[i][k])
            newMatrix.append(subMatrix)
        for k in matrix:
            for i in range(0,len(k)):
                for j in range(0,len(matrix)):
                    if k[i]==min(k) and k[i]==max(newMatrix[i]):
                        lst.append(k[i])
                        return lst
s=Solution()
print(s.luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))
                
