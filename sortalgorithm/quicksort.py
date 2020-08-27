class solution:
    def partition(self,input,low, high):
        i=low-1
        pivot= input[high]
        for j in range(low,high):
            if input[j]<pivot:
                i+=1
                input[i],input[j]=input[j],input[i]
        input[i+1],input[high]=input[high],input[i+1]
        return (i+1)

    def quick_sort(self,input,low,high):
        if len(input)==1:
            return input
        if low<high:
            pi=self.partition(input,low,high)
            self.quick_sort(input,low, pi-1)
            self.quick_sort(input,pi+1,high)
        return input
s=solution()
input=[10, 7, 8, 9, 1, 5]
print(s.quick_sort(input,0,len(input)-1))
