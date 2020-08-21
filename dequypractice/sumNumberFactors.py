class solution:
    def sumNumberFactor(self,n):
        if n==0:
            return 0
        else:
            return n%10 + self.sumNumberFactor(n/10)
s=solution()
print(s.sumNumberFactor(234))