class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        used = []
        for x in nums:
            if x in used:
                return True
            used.append(x)
        return False