class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        nums = nums[::-1]
        return nums[k - 1]
    
        # One line solution
        # return sorted(nums)[::-1][k - 1]