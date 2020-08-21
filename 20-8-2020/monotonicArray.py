# https://leetcode.com/problems/monotonic-array/
class Solution:
    def isMonotonic(self, A):
        checkInc =True
        checkDec = True
        for i in range(0,len(A)-1):
            if A[i]>A[i+1]:
                checkInc = False
        for k in range(0,len(A)-1):
            if A[k]< A[k+1]:
                checkDec = False
        if checkInc == True and checkDec == True:
            return True
        else:
            return False
        
s=Solution()
print(s.isMonotonic([1,3,2]))
            
