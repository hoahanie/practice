def nhiphan(n):
    lst=[[],['1','0'],['00','01','10','11']]
    for i in range(3,n):
        lst1=[]
        for j in lst[len(lst)-1]:
            lst1.append('0'+j)

        for j in lst[len(lst)-1]:
            lst1.append('1'+j)
       
        lst.append(lst1)
    return lst
print(nhiphan(5))

    