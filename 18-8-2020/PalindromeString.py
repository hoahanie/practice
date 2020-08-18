# https://leetcode.com/problems/construct-k-palindrome-strings/
class Solution:
    def canConstruct(self, s, k):
        a=list(s)
        if len(a)<k: return False
        else:
            d=dict()
            for i in a:
                d[i]=d.get(i,0)+1
            print (d)
            odd=0
            even=0
            for i in d:
                if d[i]%2==0:
                    even+=1
                else:
                    odd+=1
            if odd>k:
                return False
            else:
                return True
            
s=Solution()
print(s.canConstruct("leetcode", 3))