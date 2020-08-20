# https://leetcode.com/problems/monotonic-array/
class Solution:
    def isMonotonic(self, A):
        check =True
        for i in range(0,len(A)-1):
            if A[i]>A[i+1]:
                check = False
        if check == True: 
            return True
        else: 
            for k in range(0,len(A)-1):
                if A[k]< A[k+1]:
                    return False
            return True
        
s=Solution()
print(s.isMonotonic([1,3,2]))
            
