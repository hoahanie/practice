class Solution:
    def rabit(self,n):
        if n<=2:
            return 1
        else:
            return self.rabit(n-1) + self.rabit(n-2)
s=Solution()
print(s.rabit(4))
