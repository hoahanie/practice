class Solution:
    def singleNumber(self, nums):
        d=dict()
        res=[]
        for i in nums:
            d[i]=d.get(i,0)+1
        for i in d:
            if d[i]==1:
                res.append(i)
        return res
s=Solution()
print(s.singleNumber([1,2,1,3,2,5]))