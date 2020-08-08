# https://leetcode.com/problems/lucky-numbers-in-a-matrix/
class Solution:
    def luckyNumbers (self, matrix):
        newMatrix=[]
        lst=[]
        # tìm ma trận chuyển vị
        for k in range(0,len(matrix[1])):
            subMatrix=[]
            for i in range(0,len(matrix)):
                subMatrix.append(matrix[i][k])
            newMatrix.append(subMatrix)
        # tìm lucky number
        for k in matrix:
            for i in range(0,len(k)):
                for j in range(0,len(matrix)):
                    if k[i]==min(k) and k[i]==max(newMatrix[i]):
                        lst.append(k[i])
                        return lst
s=Solution()
print(s.luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))
                
