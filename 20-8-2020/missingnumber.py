class Solution:
    def missingNumber(self, nums):
        if nums == [0]:
            return 1
        if nums==[1]:
            return 0
        if len(nums)==2 :
            return max(nums)+1
        lst = range(min(nums),max(nums)+1)
        for i in lst:
            if i not in nums:
                return i
s=Solution()
print(s.missingNumber([0]))