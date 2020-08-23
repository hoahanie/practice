s='abcsdddde'
a=list(s)
d=dict()
for i in a: 
    d[i]=d.get(i,0)+1
print (d)
s1='abffgh'
b=list(s1)
for i in b:
    if i in d:
        print(i)