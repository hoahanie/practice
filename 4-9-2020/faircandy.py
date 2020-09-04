# https://leetcode.com/problems/fair-candy-swap/
class Solution:
    def fairCandySwap(self, A, B):
        sumA=sum(A)
        sumB=sum(B)
        for i in A:
            if i+(sumB-sumA)/2 in B:
                return [i,i+(sumB-sumA)/2]
s=Solution()
print(s.fairCandySwap([1,2,5],[2,4]))