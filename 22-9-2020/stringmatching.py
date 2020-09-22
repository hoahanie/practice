# https://leetcode.com/problems/string-matching-in-an-array/
class Solution:
    def stringMatching(self, words):
        res=[]
        for k in range(len(words)):
            i=0
            while i<len(words):
                if words[k] in words[i] and words[k]!= words[i]:
                    res.append(words[k])
                    break
                else:
                    i+=1
        return res
s=Solution()
print(s.stringMatching(["jak","yjakdn","tj","yyjakdn"]))