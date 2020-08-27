# https://leetcode.com/problems/sort-list/
class Solution:
    def heapify(self,head,n,i):
        largest=i
        l=2*i+1
        r=2*i+1
        if l<n and head[i]<head[l]:
            largest=l
        if r<n and head[largest]<head[r]:
            largest=r
        if largest!=i:
            head[i],head[largest]=head[largest],head[i]
            self.heapify(head,n,largest)
    def sortList(self, head):
        n=len(head)
        for i in range(n//2-1,-1,-1):
            self.heapify(head,n,i)
        for i in range(n-1,0,-1):
            head[i],head[0]=head[0],head[i]
            self.heapify(head,i,0)
        return head
s=Solution()
print(s.sortList(4->2->1->3))
