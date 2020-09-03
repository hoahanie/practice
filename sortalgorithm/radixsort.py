class solution:
    def counting_sort(self,arr, exp1):
        n=len(arr)
        output=[0]*n
        count=[0]*(10)

        for i in range(0,n):
            index = (arr[i]/exp1)
            count[(index)%10] +=1
        for i in range(1,10):
            count[i]+=count[i-1]
        print(count)
        i=n-1
        while i>=0:
            index = (arr[i]/exp1)
            output[count[(index)%10]-1]=arr[i]
            print(count[(index)%10], "..")
            print(count[(index)%10]-1)
            count[(index)%10]-=1
            i-=1
        i=0
        print(output)
        print("**")
        for i in range(len(arr)):
            arr[i]=output[i]
        print(arr)
        print("end")
    def radix_sort(self,arr):
        max1=max(arr)
        exp=1
        while max1/exp>0:
            self.counting_sort(arr,exp)
            exp*=10
        return arr
s=solution()
print(s.radix_sort([ 170, 45, 75, 90, 802, 24, 2, 66] ))