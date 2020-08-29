# https://leetcode.com/problems/permutation-in-string/
class Solution:
    def checkInclusion(self, s1, s2):
        d1=dict()
        for i in s1:
            d1[i]=d1.get(i,0)+1
        for i in range(0,len(s2)-len(s1)+1):
            a=(s2[i:i+len(s1)])
            print(a)
            d2=dict()
            for j in a:
                d2[j]=d2.get(j,0)+1
            if d2==d1:
                return True
            # check=True
            # for k in d1:
            #     if k not in d2 or d1[k]!=d2[k]:
            #         check=False
            # if check== True:
            #     return True
        return False 
s=Solution()
print(s.checkInclusion("adc","dcda"))

