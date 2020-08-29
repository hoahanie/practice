# https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/practice-problems/algorithm/help-natsu/description/
from __future__ import print_function
class solution:
    def help_natsu(self,n):
        d=dict()
        for i in n:
            d[i]=d.get(i,0)+1
        t=sorted(zip(d.values(),d.keys()))
        for k,v in t:
            print(k,v )

# T = input()
# for i in range(T):
#     s=solution()
#     numOfTask = input()
#     listTask =[]
#     for j in range(numOfTask):
#         listTask.append(input())
#     s.help_natsu(listTask)
    

s=solution()

print(s.help_natsu(['abcd','bcd','abc','abc','abc','bcd','bge','dbaa','bcd','bge']))