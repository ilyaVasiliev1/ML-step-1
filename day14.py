class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0
        while x:
            rev = rev * 10 + x % 10
            x //= 10
        res = sign * rev
        return res if -2**31 <= res <= 2**31 - 1 else 0
    
# математическое решенеи