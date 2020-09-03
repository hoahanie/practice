class solution:
    def counting_sort(self,input):
        output= [0 for i in range(256)]
        count=[0 for i in range(256)]
        ans = ["" for _ in input] 
        for i in input:
            count[ord(i)]+=1
        for i in range(256):
            count[i]+=count[i-1]
        print(count)
        for i in range(len(input)):
            output[count[ord(input[i])]-1]=input[i]
            count[ord(input[i])]-=1

        print(output)
        for i in range(len(input)):
            ans[i]=output[i]
        res ="".join(ans)
        
        return res


s=solution()
print(s.counting_sort("geeksforgeeks"))