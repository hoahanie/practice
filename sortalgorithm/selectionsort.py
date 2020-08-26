class solution:
    def selection_sort(self,n):
        for i in range(len(n)):
            min_index=i
            for k in range(i+1,len(n)):
                if n[min_index]>n[k]:
                    min_index=k
            n[i],n[min_index]=n[min_index], n[i]
        return n
s=solution()
print(s.selection_sort([19,2,31,45,30,11,121,27]))