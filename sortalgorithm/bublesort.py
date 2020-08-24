class solution:
    def bulblesort(self,n):
        for i in range(0,len(n)-1):
            for j in range(i+1,len(n)):
                if n[i]>n[j]:
                    temp=n[i]
                    n[i]=n[j]
                    n[j]=temp
        return n
s=solution()
print(s.bulblesort([64, 34, 25, 12, 22, 11, 90] ))
