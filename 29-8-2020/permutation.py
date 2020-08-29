# https://leetcode.com/problems/permutations/
class Solution:
    res=[]
    def permute(self, nums):
        self.res=[]
        output=[0]*len(nums)
        visited=[False]*(len(nums))
        self.recursion(nums,0,visited,output)
        return self.res

    def recursion(self, nums, pos, visited,output):
        for i in range(len(nums)):
            if visited[i] == False:
                visited[i] = True
                output[pos]=nums[i]
                if pos==len(nums)-1:
                    temp=[]
                    for k in output:
                        temp.append(k)
                    self.res.append(temp)
                else:
                    self.recursion(nums,pos+1,visited,output)
                visited[i]=False
s=Solution()
print(s.permute([1,2,3]))



        