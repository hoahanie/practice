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
        if self.graph:
            return max(self.graph)+1
        return 0

    def DFS(self,v,check,lst):
        visited =[False]*(max(self.graph)+1)
        self.DFSUtil(v,visited,check,lst)


class Solution:
    def swap(self,s,pairs):
        g = graph()
        for i in pairs:
            g.addEdge(i[0],i[1])
            g.addEdge(i[1],i[0])
    
        check = [False]*g.getLen()
        res = []
        for i in range(g.getLen()):
            lst = []
            if check[i]==False:
                g.DFS(i,check,lst)
                res.append(lst)
        s = list(s)
        for i in res:
            i.sort()
            B = [s[k] for k in i]
            B.sort()
            for j in range(len(B)):
                s[i[j]] = B[j]
        return "".join(s)
s = Solution()
print(s.swap("dcab",[[0,3],[1,2],[0,2]]))

