from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        min_price = float("inf")
        for p in prices:
            if p < min_price:
                min_price = p
            else:
                best = max(best, p - min_price)
        return best