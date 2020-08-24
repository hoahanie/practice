# https://leetcode.com/problems/number-of-matching-subsequences/
class Solution:
    def dictionary(self,n):
        c=list(n)
        b=dict()
        for i in c:
            b[i]=b.get(i,0)+1
        return b
    def numMatchingSubseq(self, S, words):
        d=dict()
        a=list(S)
        for i in a:
            d[i]=d.get(i,0)+1
        dem=0
        for i in words:
            check=True
            e=self.dictionary(i)
            for i in e:
                if i in d and e[i]<=d[i]:
                    check= True
                else:
                    check = False
            if check== True:
                dem+=1
        return dem
s=Solution()
print(s.numMatchingSubseq("btovxbkumc",["btovxbku","to","zueoxxxjme","yjkclbkbtl"]))