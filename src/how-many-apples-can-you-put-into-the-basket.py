class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        arr.sort()
        weight = 0
        apples = 0
        for num in arr:
            if weight < 5000 and weight + num < 5000:
                weight += num
                apples += 1
        return apples