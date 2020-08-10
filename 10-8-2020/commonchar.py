class Solution:
    def commonChars(self, A):
        B=[]
        lst=[]
        #chuyen cac phan tu cua A thanh list
        for i in A:
            B.append(list(i))
        #lay tung phan tu cua B[0] dem check co nam trong cac phan tu con lai cua B khong
        i=0
        for i in B[0]:
            for k in B:
                if i in k:
                    k.remove(i)
                else:
                    break
            lst.append(i)
        return lst
s=Solution()
print(s.commonChars(["bella","label","roller"]))