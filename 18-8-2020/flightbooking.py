# https://leetcode.com/problems/corporate-flight-bookings/
class Solution:
    def corpFlightBookings(self, bookings, n):
        lst =range(1,n+1)
        d=dict()
        for i in lst:
            d[i]=d.get(i,0)
        for i in bookings:
            for k in range(i[0],i[1]+1):
                d[k]+=i[2]
        return d.values()

s=Solution()
print(s.corpFlightBookings([[1,2,10],[2,3,20],[2,5,25]],5))