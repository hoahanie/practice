class Solution:
    def makeGood(self, s):
        if len(s)==0 or len(s)==1:
            return s
        else:
            lst =list(s)
            i=0
            while i<len(lst)-1:
                if abs(ord(lst[i])-ord(lst[i+1])) == 32:
                    lst =lst[0:i] +lst[i+2:]
                    # lst.remove(lst[i])
                    # lst.remove(lst[i])
                    i=0
                else:
                    i=i+1
            a= "".join(lst)
            return a
s=Solution()
print(s.makeGood("djrDdRJD"))