class Solution:
    def luckyNumbers (self, matrix):
        newMatrix=[]
        for k in range(0,len(matrix[1])):
            subMatrix=[]
            for i in range(0,len(matrix)):
                subMatrix.append(matrix[i][k])
            newMatrix.append(subMatrix)

        return newMatrix
s=Solution()
print(s.luckyNumbers([[7,8],[1,2]]))
                