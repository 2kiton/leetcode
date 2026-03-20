from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numseen = set()
        for n in nums:
            if n in numseen:
                return True
            numseen.add(n)
        
        return False