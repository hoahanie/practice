# https://leetcode.com/problems/string-compression/
class Solution:
    def compress(self, chars):
        d=dict()
        res =[]
        lst=[]

        for i in chars:
            d[i]=d.get(i,0)+1
        for i in chars:
            if i not in lst:
                lst.append(i)
        for i in lst:
            if d[i]==1:
                res.append(i)
            else:
                res.append(i)
                res.append(str(d[i]))
        dem =0
        for i in res:
            dem+= len(i)
        return dem, res        

s=Solution()
print(s.compress(["a","a","b","b","c","c","c","c","c","c","c","c","c","c","c","c"]))
