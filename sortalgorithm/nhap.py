class solution:
    def insert_sort(self,b):
        for i in range(1,len(b)):
            up=b[i]
            j=i-1
            while j>=0 and b[j]>up:
                b[j+1]=b[j]
                j-=1
            b[j+1]=up
        return b
s=solution()
print(s.insert_sort([ 0.665, 0.656] ))