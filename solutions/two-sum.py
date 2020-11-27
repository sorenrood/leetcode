class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ### Brute Force
        length = len(nums)
        for i in range(0, length):
            for j in range(0, length):
                if i == j:
                    continue
                a = nums[i]
                b = nums[j]
                if a + b == target:
                    return [i,j]
                
        ### Better solution
        # Create map
        dict = {}
        
        # Add things to map
        for i in range(0, len(nums)):
            dict[nums[i]] = i
        
        # loop and solve
        for i in range(0, len(nums)):
            complement = target - nums[i]
            if complement in dict and dict.get(complement) != i:
                return [i, dict.get(complement)]