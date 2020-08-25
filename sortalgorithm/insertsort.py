class solution:
    def insert_sort(self,n):
        for i in range(1, len(n)):
            j=i-1
            temp= n[i]
            while (n[j]> temp) and( j>=0):
                n[j+1]=n[j]
                j=j-1
            n[j+1]=temp
        return n

s=solution()
print(s.insert_sort([19,2,31,45,30,11,121,27]))
