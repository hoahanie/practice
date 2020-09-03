class Solution:
    def groupThePeople(self, groupSizes):
        d=dict()
        for i in range(0,len(groupSizes)):
            if groupSizes[i] not in d:
                d[groupSizes[i]]=[]
            if groupSizes[i] in d:
                d[groupSizes[i]]+=[i]
        return d
s=Solution()
print(s.groupThePeople([3,3,3,3,3,1,3]))