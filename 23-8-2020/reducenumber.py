# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/
class Solution:
    def numSteps(self, s):
        a=int(s,2)
        print(a)
        dem=0
        while a!=1:
            if a%2==1:
                a=a+1
                dem+=1
            if a%2== 0:
                a=a/2
                dem+=1
        return dem
s=Solution()
print(s.numSteps(
"1111011110000011100000110001011011110010111001010111110001"))
