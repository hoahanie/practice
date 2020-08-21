class solution:
    def sumNumberFactor(self,n):
        if n==0:
            return 0
        else:
            if n%2 ==0:
                return n+ self.sumNumberFactor(n-2)
            else:
                return n-1 +self.sumNumberFactor(n-3)
s=solution()
print(s.sumNumberFactor(6))