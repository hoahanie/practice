# https://leetcode.com/problems/search-suggestions-system/
class Solution:
    def divideSearchWord(self,searchWord):
        newWord=[]
        for i in range(1,len(searchWord)+1):
            a=searchWord[0:i]
            newWord.append(a)
        return newWord
    def bubleSort(self,n):
        if len(n)==1: 
            return n
        if len(n)<=3 and len(n)>=2:
            n.sort()
            return n
        else:
            n.sort()
            return n[0:3]

        
    def suggestedProducts(self, products, searchWord):
        res =[]
        b=self.divideSearchWord(searchWord)
        for i in range(0,len(b)):
            lst=[]
            for j in range(len(products)):
                if products[j][0:len(b[i])]==b[i]:
                    lst.append(products[j])
            res.append(lst)
        print(res)
        final=[]
        for i in res:
            a=self.bubleSort(i)
            final.append(a)

        return final

s=Solution()
print(s.suggestedProducts(["bags","baggage","banner","box","cloths"] ,"bags"))
