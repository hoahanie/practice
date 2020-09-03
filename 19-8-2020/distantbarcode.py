class Solution:
    def rearrangeBarcodes(self, barcodes):
        d=dict()
        res = []
        for i in barcodes:
            d[i] = d.get(i,0) + 1
        for i in d:
            res.append(i)
            d[i]-=1
        return d
s=Solution()
print(s.rearrangeBarcodes( [1,1,1,2,2,2]))
