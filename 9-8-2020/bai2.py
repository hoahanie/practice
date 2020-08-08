class Solution:
    def sortString(self, s):
        a=sorted(set(list(s)))
        b=sorted(s)
        lst=[]
        count=dict()
        for i in a:
            count[i]=0
        for i in b:
            count[i]+=1
        res=[]
        while True:
            for i in a:
                if count[i]>=1:
                    res.append(i)
                    count[i]-=1
            for i in range(len(a)-1,-1,-1):
                if count[a[i]]>=1:
                    res.append(a[i])
                    count[a[i]]-=1
            if len(res)==len(s): break
        return "".join(res)
s=Solution()
print(s.sortString("aaaabbbbcccc"))


            