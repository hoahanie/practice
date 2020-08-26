class solution:
    def counting_sort(self,input):
        count = [0 for i in range(max(input)+1)]
        output=[0 for i in range(max(input)+1)]
        res =['' for _ in input]
        for i in input:
            count[i]+=1
        for i in range(max(input)+1):
            count[i]+=count[i-1]
        print(count)
        for i in range(len(input)):
            output[count[input[i]]-2]=input[i]
            print(count[input[i]])
            count[input[i]]-=1

        print(output)
        for i in range(len(input)):
            res[i]=output[i]
        print(res)
        return
s=solution()
print(s.counting_sort([9,6,3,5,0]))

