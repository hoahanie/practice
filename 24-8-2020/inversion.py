class solution:
    def countInver(self,a):
        lst=[]
        for i in range(0,len(a)-1):
            c=[]
            for k in range(i+1,len(a)):
                if a[i]>a[k]:
                    c.append(a[i])
                    c.append(a[k])
                    lst.append(tuple(c))
                    c=[]
        return lst
s=solution()
print(s.countInver([8, 4, 2, 1]))
            