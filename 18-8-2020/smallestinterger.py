# https://leetcode.com/problems/smallest-integer-divisible-by-k/
class Solution:
    def smallestRepunitDivByK(self, K):
        lst =[2,4,5,6,8]
        for i in lst:
            if K%i==0:
                return -1
        else:
            lst ='1'
            i=len(str(K))
            while True:
                a =int(lst*i)
                if a%K!=0:
                    i+=1
                else:
                    return len(str(a))
                    break
s=Solution()
print(s.smallestRepunitDivByK(19927))
