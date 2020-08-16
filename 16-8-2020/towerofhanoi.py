def towerofhanoi(n,source,destination,aux):
    if n==1:
        print("move 1 from", source, "to" ,destination)
        return
    else:
        towerofhanoi(n-1,source,aux,destination)
        print("move",n," from",source,"to",destination)
        towerofhanoi(n-1,aux,destination,source)
towerofhanoi(4,'A','B','C')
        