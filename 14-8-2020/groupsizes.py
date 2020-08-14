class Solution:
    def groupThePeople(self, groupSizes):
        d=dict()
        for i in range(0,len(groupSizes)):
            if groupSizes[i] not in d:
                d[groupSizes[i]]=[]
            if groupSizes[i] in d:
                d[groupSizes[i]]+=[i]
        res=[]
        for i in d:
            if len(d[i])==i:
                res.append(d[i])
            else:
                subRes =[]
                for k in range(0,len(d[i])):
                    subRes.append(d[i][k])
                    if len(subRes)==i:
                        res.append(subRes)
                        subRes=[]
        return res
s=Solution()
print(s.groupThePeople([3,3,3,3,3,1,3]))
                

