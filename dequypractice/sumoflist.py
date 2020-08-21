class solution:  
    def sumList(self,n):
        if len(n) ==1:
            return n[0]
        else:
            return n[0]+ self.sumList(n[1:])
s= solution()
print(s.sumList([1,2,3,4,5]))