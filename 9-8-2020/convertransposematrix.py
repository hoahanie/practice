# tìm ma trận chuyển vị
class Solution:
    def luckyNumbers (self, matrix):
        # Tạo ma trận chuyển vị
        newMatrix=[]
        for k in range(0,len(matrix[1])):
            subMatrix=[]
            for i in range(0,len(matrix)):
                subMatrix.append(matrix[i][k])
            newMatrix.append(subMatrix)

        return newMatrix
s=Solution()
print(s.luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))
                