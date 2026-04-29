class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # approach 1 -- sort array and count diff
        if len(nums) == 0:
            return 0

        nums = sorted(set(nums))
        print(nums)
        max_count = 0
        count = 0
        prev = nums[0]

        for n in nums:
            if n - prev == 1:
                count+=1
                prev = n
            else:
                count = 0
                prev = n
            max_count = max(max_count, count)
        return max_count+1