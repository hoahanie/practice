# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
class solution:
    def heapify(self,i,arr,n):
        maxNum=i
        l=2*i+1
        r=2*i+2
        if l<n and arr[l]<arr[i]:
            maxNum=l
        if r<n and arr[r]<arr[maxNum]:
            maxNum=r
        if maxNum!= i:
            arr[maxNum],arr[i]=arr[i],arr[maxNum]
            self.heapify(maxNum,arr,n)       

    def heap_sort(self,arr):
        n=len(arr)
        for i in range(n//2-1,-1,-1):
            self.heapify(i,arr,n)
        for i in range(n-1,0,-1):
            arr[i],arr[0]=arr[0],arr[i]
            self.heapify(0,arr,i)
        return arr
    def maxCoins(self,piles):
        n=len(piles)
        self.heap_sort(piles)
        sum=0
        for i in range(0,n/3):
            sum+=piles[2*i+1]
        return sum

s=solution()
print(s.maxCoins([2,4,5]))

