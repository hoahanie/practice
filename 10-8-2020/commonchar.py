# https://leetcode.com/problems/find-common-characters/
class Solution:
    def commonChars(self, A):
        B=[]
        lst=[]
        res =[]
        for i in A:
            lst =list(str(i))
            B.append(lst)
            lst=[]
        for i in B[0]:
            for k in B:
                if i not in k:
                    break
            else:
                res.append(i)
                for x in range (1,len(B)):
                    for n in range(0,len(B[x])):
                        if B[x][n]==i:
                            B[x].remove(i)
                            break  
        return res
        
s=Solution()
print(s.commonChars(["bella","label","roller"]))