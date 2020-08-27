class solution:
    def heapify(self,arr,n,i):
        largest = i
        l=2*i+1
        r=2*i+2
        if l<n and arr[i]<arr[l]:
            largest=l
        if r<n and arr[largest]<arr[r]:
            largest=r
        if largest!=i:
            arr[i],arr[largest]=arr[largest],arr[i]
            self.heapify(arr,n,largest)
    def heap_sort(self,arr):
        n=len(arr)
        for i in range(n//2 - 1,-1,-1):
            self.heapify(arr,n,i)
        for i in range(n-1,0,-1):
            arr[i],arr[0]=arr[0],arr[i]
            self.heapify(arr,i,0)
        return arr
s=solution()
arr=[ 12, 11, 13, 5, 6, 7]
n=len(arr)
print(s.heap_sort( arr ))
        
