class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        front = nums[0] * nums[1] * nums[2]
        back = nums[0] * nums[-1] * nums[-2]
        return max(front, back)