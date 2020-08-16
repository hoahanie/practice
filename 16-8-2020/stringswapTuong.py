# https://leetcode.com/problems/smallest-string-with-swaps/
from collections import defaultdict
class graph:
    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def DFSUtil(self,v,visited,check,lst):
        visited[v]=True
        check[v]=True
        lst.append(v)
        for i in self.graph[v]:
            if visited[i]==False:
                self.DFSUtil(i,visited,check,lst)
           

    def getLen(self):
        return max(self.graph)+1

    def DFS(self,v,check,lst):
        visited =[False]*(max(self.graph)+1)
        self.DFSUtil(v,visited,check,lst)


class Solution:
    def swap(self,s,pairs):
        g = graph()
        for i in pairs:
            g.addEdge(i[0],i[1])
            g.addEdge(i[1],i[0])
        print(g.graph)
    
        check = [False]*g.getLen()
        res = []
        for i in range(g.getLen()):
            lst = []
            if check[i]==False:
                g.DFS(i,check,lst)
                res.append(lst)
        print(res)
        listSet = []
        for i in res:
            s1=[]
            for j in i:
                s1.append(s[j])
            listSet.append(s1)
        print(listSet)
        for i in range(len(listSet)):
            listSet[i].sort()
        listSet.sort()
        print(listSet)
        kq = ''
        for i in listSet:
            for j in i:
                kq+=j
            
        return kq

    def countMax(self,pairs):
        maxPairs=pairs[0][0]
        for i in pairs:
            for j in i:
                if j>maxPairs:
                    maxPairs=j
        return maxPairs

s = Solution()
print(s.swap("cba",[[0,1],[1,2]]))