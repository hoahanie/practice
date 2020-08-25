class solution:
    def merge_sort(self,n):
        if len(n)<=1:
            return n
        mid_list = len(n)//2
        left_list = n[:mid_list]
        right_list = n[mid_list:]
        left_list=self.merge_sort(left_list)
        right_list=self.merge_sort(right_list)
        return self.merge(left_list,right_list)
    def merge(self,left_half,right_half):
        res =[]
        while len(left_half)!=0 and len(right_half)!=0:
            if left_half[0]<right_half[0]:
                res.append(left_half[0])
                left_half.remove(left_half[0])
            else:
                res.append(right_half[0])
                right_half.remove(right_half[0])
        if len(left_half)==0:
            res= res+right_half
        if len(right_half)==0:
            res= res+left_half
        return res
s=solution()
print(s.merge_sort([64, 34, 25, 12, 22, 11, 90]))