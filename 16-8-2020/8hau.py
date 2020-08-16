n=5
a=[True]*(n+1)
b=[True]*2*(n+1)
c=[True]*2*(n)
x=[0]*(n+1)
def try8hau(i):
    for j in range(1,n+1):
        if a[j]==True and b[i+j]==True and c[i-j]==True:
            x[i]=j
            if i==n:
                print(x)
            else:
                a[j]=False
                b[i+j]=False
                c[i-j]=False
                try8hau(i+1)
                a[j]=True
                b[i+j]=True
                c[i-j]=True
try8hau(1)

