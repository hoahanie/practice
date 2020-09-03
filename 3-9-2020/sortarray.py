# https://leetcode.com/problems/sort-array-by-parity-ii/
class Solution:
    def sortArrayByParityII(self, A):
        even=[]
        odd = []
        for i in A:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        res =[]
        while len(odd)!=0:
            res.append(even[len(even)-1])
            even.pop()
            res.append(odd[len(odd)-1])
            odd.pop()
        return res
s=Solution()
print(s.sortArrayByParityII([4,2,5,7]))
        