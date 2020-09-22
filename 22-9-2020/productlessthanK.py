# https://leetcode.com/problems/subarray-product-less-than-k/
class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        count =0
        for i in range(len(nums)):
            count += self.countProduct(nums[i:],k)
        return count

    def countProduct(self, num,k):
        s=1
        j=0
        count1=0
        while j<len(num):
            if s*num[j]<k:
                s=s*num[j]
                count1+=1
                j+=1
            else:
                break
        return count1

s=Solution()
print(s.numSubarrayProductLessThanK([5, 2, 6], 100))
        


         
