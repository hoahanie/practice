class solution:
    def towerofhanoi(self,n,source, destination,aux):
        if n==1:
            print("move disk 1 from sourse", source, "to destination", destination)
            return
        else:
            self.towerofhanoi(n-1,source,aux,destination)
            print("move disk",n, "from",source, "to", destination)
            self.towerofhanoi(n-1, aux, destination,source)
s=solution()
print(s.towerofhanoi(3,'A','B','C'))