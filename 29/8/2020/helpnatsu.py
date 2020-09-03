# https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/practice-problems/algorithm/help-natsu/description/
class solution:
    def help_natsu(self,n):
        count=[]
        for i in range(len(n)):
            count.append([])
        a=set(n)
        dem=0
        print(count)
        print(a)
        for i in a:
            for j in n:
                if j==i:
                    dem+=1
            count[dem].append(i)
            dem=0
        return count
    def sorting(self,k):
        output=[]
s=solution()
print(s.help_natsu(['abcd','bcd','abc','abc','abc','bcd','bge','dbaa','bcd','bge']))