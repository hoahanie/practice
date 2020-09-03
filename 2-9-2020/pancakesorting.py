# https://leetcode.com/problems/pancake-sorting/
class Solution:
    def pancakeSort(self, arr):
        maxNum = arr[0]
        pos = 0
        for i in range(1, len(arr)):
            if arr[i] > maxNum:
                maxNum = arr[i]
                pos = i
        print(pos)
        temp = arr[0:pos+1]
        temp.reverse()
        arr = temp + arr[pos+1:]
        arr.reverse()
        print(arr)
        check = True
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                check = False
        if len(arr) == 2:
            if pos == 0:
                return [2]
            else:
                return []
        if check == True:
            return []
        else:
            return [pos+1, len(arr)] + self.pancakeSort(arr[0:len(arr)-1])
        # check=True
        # for i in range(0,len(arr)-1):
        #     if arr[i]>arr[i+1]:
        #         check=False
        # if check == True:
        #     return []
        # else:
        #     res=[]
        #     for i in range(len(arr)-1,0,-1):
        #         maxNum = arr[0]
        #         pos = 0
        #         for i in range(1, len(arr)):
        #             if arr[i] > maxNum:
        #                 maxNum = arr[i]
        #                 pos = i
        #         res.append(pos)
        #         temp = arr[0:pos+1]
        #         temp.reverse()
        #         res.append(len(arr))
        #         arr = temp + arr[pos+1:]
        #         arr.reverse()
        # return arr
s = Solution()
print(s.pancakeSort([3, 2, 4, 1]))
