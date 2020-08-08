class Solution:
    def sortString(self, n):
        lst=[]
        lst.append(1)
        lst.append(1)
        for i in range(2,n):
            lst.append(lst[i-2]+lst[i-1])
        return lst
s=Solution()
print(s.sortString(10))

