class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = {}

        for i in nums:
            if i not in counter:
                counter[i] = 1
            elif i in counter:
                return True
        
        return False

