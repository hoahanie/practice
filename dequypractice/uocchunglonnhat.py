class solution:
    def gcd (self,x,y):
        if y==0:
            return x
        else:
            return self.gcd(y,x%y)
s=solution()
print(s.gcd(12,56))