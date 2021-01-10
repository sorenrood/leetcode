class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        rec = {}
        for x in nums:
            if x not in rec:
                rec[x] = 1
            else:
                return True
        return False