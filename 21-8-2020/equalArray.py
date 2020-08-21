# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/
class Solution:
    def canBeEqual(self, target,arr):
        if sorted(arr)== sorted(target):
            return True
        return False
s=Solution()
print(s.canBeEqual([1,2,3,4],  [2,4,1,3]))