class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        mappings = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in mappings:
                return [mappings[complement], i]
            mappings[num] = i 
        
        return []

        
        