class Solution:
    dem=0
    def checkIncreasing(self,rating):
        for i in range(0,len(rating)-2):
            for j in range(i+1,len(rating)-1):
                for k in range(j+1,len(rating)):
                    if rating[i]>rating[j] and rating[j]>rating[k]:
                        self.dem+=1

    def checkDecreasing(self,rating):
        for i in range(0,len(rating)-2):
            for j in range(i+1,len(rating)-1):
                for k in range(j+1,len(rating)):
                    if rating[i]<rating[j] and rating[j]<rating[k]:
                        self.dem+=1
    def numTeams(self, rating):
        self.checkIncreasing(rating)
        self.checkDecreasing(rating)
        return self.dem
s=Solution()
print(s.numTeams([2,1,3]))
            
            
