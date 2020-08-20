# https://leetcode.com/problems/minimum-index-sum-of-two-lists/
class Solution:
    def findRestaurant(self, list1, list2):
        d=dict()
        for i in range(0,len(list1)):
            value =[]
            for j in range(0,len(list2)):
                if list1[i]==list2[j]:
                    value.append(i+j)
                    d[list1[i]]= value
        for i in d:
            if d[i]== min(d.values()):
                return i
s=Solution()
print(s.findRestaurant([ "KFC","Shogun", "Tapioca Express", "Burger King"],["KFC", "Shogun", "Burger King"]))