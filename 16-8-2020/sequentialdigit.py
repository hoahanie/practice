# https://leetcode.com/problems/sequential-digits/
class Solution:
    # def sequentialDigits(self, low, high):
    #     lst=[]
    def findNumber(self,lst):
        num=[]
        for i in range(0,len(lst)-1):
            num.append(int("".join(lst[i:i+2])))   
        return num
s=Solution()
print(s.findNumber([s1,2,3,4,5,6,7,8,9]))
            