# https://leetcode.com/problems/maximum-subarray/
# class Solution:
    # def findArraySum(self,nums,n):
    #         lst =[]
    #         for k in range(n,len(nums)):
    #             if nums[k] not in lst:
    #                 lst.append(nums[k])
    #             else:
    #                 break
    #         return sum(lst)
    # def maxSubArray(self, nums):
    #     maxArray =0
    #     for i in range(0,len(nums)):
    #         if self.findArraySum(nums,i) >maxArray:
    #             maxArray = self.findArraySum(nums,i)
    #     return maxArray
class Solution:
    def maxSubArray(self, A):
        for i in range(1,len(A)):
            if A[i-1]>0:
                A[i]+=A[i-1]
                
        print(A)
        return max(A)       
s=Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))