class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            x = str(x)
            return x == x[::-1] #разворот строки 
        else:
            return False
        

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1] # в приницпе то же самое, только быстрее