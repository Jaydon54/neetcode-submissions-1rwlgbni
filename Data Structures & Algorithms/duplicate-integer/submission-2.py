class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_appeared = []

        for n in nums:
            if n in has_appeared:
                return True
            has_appeared.append(n)
        return False
        