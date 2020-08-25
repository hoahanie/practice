class solution:
    def shell_sort(self, n):
        gap = len(n)//2
        while gap>0:
            print("gap= ", gap)
            for i in range(gap, len(n)):
                print("i =",i)
                temp= n[i]
                j=i
                while j>= gap and n[j-gap]>temp:
                    n[j]= n[j-gap]
                    j=j-gap
                n[j]=temp
                print("n =", n)
            gap=gap//2
        return n
s=solution()
print(s.shell_sort([19,2,31,45,30,11,121,27]))