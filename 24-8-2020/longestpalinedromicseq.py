class Solution:
    # def longestPalindromeSubseq(self, s):
    
    def findPalindromSubseq(self,n):
        if len(n)==1 or len(n)==0:
            return n
        if len(n)==2:
            if n[0]==n[1]:
                return n
            else:
                return n[0]
        else:
            lst=[]
            for i in range(1,len(n)-1):
                for j in range(min((i-0),(len(n)-1-i))):
                    c=''
                    if n[i-i]==n[i+j]:
                        c+=n[i-j:i+j+1]
                        lst.append(c)
        return lst
s=Solution()
print(s.findPalindromSubseq("cbbd"))

