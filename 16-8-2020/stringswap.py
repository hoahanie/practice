# https://leetcode.com/problems/smallest-string-with-swaps/
class Solution:
    def arrangePairs(self,pairs):

    def countMax(self,pairs):
        maxPairs=pairs[0][0]
        for i in pairs:
            for j in i:
                if j>maxPairs:
                    maxPairs=j
        return maxPairs

class graph:
    def __init__(self): 
        self.graph = defaultdict(list) 
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def DFSUtil(self,v,visited):
        visited[v]=True
        for i in self.graph[v]:
            if visited[i]==False:
                self.DFSUtil(i,visited)

    def DFS(self,v):
        visited =[False]*(max(self.graph)+1)
        self.DFSUtil(v,visited)

