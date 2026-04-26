class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for index, val in enumerate(nums):
            if target-val in dict:
                return [dict[target-val], index]
            else:
                dict[val] = index
            
        return [-1,-1]