from __future__ import print_function
#be them cai thu vien ni vo khong hieu ren python be chi nhan python 2 
class solution:
    def sloveX(self,n):
        if n==1:
            print(n, end = "")
        else:
            if n%2==0:
                self.sloveX(n//2)
                print('*2',end="")
            else:
                self.sloveX(n*3 +1)
                print('/3',end="")
s=solution()
s.sloveX(10)
