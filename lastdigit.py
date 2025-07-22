class Solution:
    def lastDigit(self, n: int) -> int:
        #Code here
        last = abs(n) % 10
        return last
s=Solution()
print(s.lastDigit(123))
