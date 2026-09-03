class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        pool = set()
        for char in nums:
            if char in pool:
                return True
            pool.add(char)
            print(f"Added {char}")
        return False