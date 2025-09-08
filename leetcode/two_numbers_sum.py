from typing import Dict, List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: Dict[int, int] = {} #число - индекс 
        for i, x in enumerate(nums):
            need = target - x # 9 - x, и если есть, то сразу индекс 
            if need in seen:
                return [seen[need], i]
            seen[x] = i
        return[]
    
