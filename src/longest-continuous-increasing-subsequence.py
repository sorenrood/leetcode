class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        prev = -math.inf
        result = 0
        count = 0
        for num in nums:
            if num > prev:
                count += 1
            else:
                count = 1
            prev = num
            result = max(result, count)
        return res