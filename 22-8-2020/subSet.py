#https://leetcode.com/problems/subsets/
class Solution:
    res = list()
    
    def __init__(self):
        self.res = list()
        self.res.append([])
        
    def recursion(self, nums, index, output, visit):
        if index == len(nums):
            return 
        visit[index] = True
        output.append(nums[index])
        a = []
        for i in output:
            a.append(i)
        self.res.append(a)
        print(output)
        
        self.recursion(nums,index+1,output,visit)
        output.pop()
        if index+1!=len(nums):
            visit[index]=False
            self.recursion(nums,index+1,output,visit)

    def subsets(self, nums):
   
        output= []
        visit = [False]*len(nums)
        self.recursion(nums,0,output,visit)
        return self.res

s = Solution()
print(s.subsets([1,2,3]))