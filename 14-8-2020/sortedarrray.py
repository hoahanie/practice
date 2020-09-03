# https://leetcode.com/problems/single-element-in-a-sorted-array/
class Solution:
    def singleNonDuplicate(self, nums):
        d=dict()
        for i in nums:
            d[i]=d.get(i,0)+1
        for i in d:
            if d[i]==1:
                return i
s=Solution()
print(s.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
