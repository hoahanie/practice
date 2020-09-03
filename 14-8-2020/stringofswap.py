# https://leetcode.com/problems/smallest-string-with-swaps/
class Solution:
    def smallestStringWithSwaps(self, s,pairs):
        a=list(s)
        while True:
            check=True
            for i in pairs:
                if a[i[0]]>a[i[1]]:
                    a[i[0]],a[i[1]]=a[i[1]],a[i[0]]
                    check = False
            if check==True: break
        return "".join(a)    
s=Solution()
print(s.smallestStringWithSwaps("dcab", [[0,3],[1,2],[0,2]]))