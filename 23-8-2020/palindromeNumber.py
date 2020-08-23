class Solution:
    def isPalindrome(self, x):
        if x<0: return False
        elif len(str(x))==1: return True
        else:
            check =True
            s=list(str(x))
            for i in range(0,len(s)//2):
                if s[i]!=s[len(s)-1-i]:
                    check =False
            if check == True:
                return True
            else:
                return False
s=Solution()
print(s.isPalindrome(123123))
