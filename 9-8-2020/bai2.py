class Solution:
    def sortString(self, s):
        a=sorted(set(list(s)))
        b=sorted(s)
        lst=[]
        count=dict()
        for k in range(0,len(a)):
            dem=0
            for i in range(0,len(b)):
                if b[i]==a[k]: 
                    dem+=1
            lst.append(dem)
        for key in a:
            for value in lst:
                count[key]=value
                lst.remove(value)
                break
        res=[]
        while len(res)<len(b):
            for k in count.keys():
                if count[k]>0:
                    res.append(k)
                    count[k]-=1
            for k in reversed(count.keys()):
                if count[k]>0:
                    res.append(k)
                    count[k]-=1
        return count
s=Solution()
print(s.sortString("aaaabbbbcccc"))


            