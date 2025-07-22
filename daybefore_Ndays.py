class Solution:
    def findAnswer(self, d, n):
       #Code here
       ans = (d-n) % 7
       return ans
s=Solution()
print(s.findAnswer(0,9))
