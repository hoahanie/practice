class Solution:
    def tribonacci(self, n):
        # if n ==0:
        #     return 0
        # if n == 1:
        #     return 1
        # if n ==2:
        #     return 1
        # else:
        #     return self.tribonacci(n-3)+self.tribonacci(n-2)+self.tribonacci(n-1)
        lst =[0,1,1]
        for i in range(3,n+1):
            lst.append(lst[len(lst)-1]+lst[len(lst)-2]+lst[len(lst)-3])
        return lst[n]
s=Solution()
print(s.tribonacci(5))