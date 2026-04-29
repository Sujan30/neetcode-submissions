class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # empty array
        if not nums:
            return 0

        curr_seq = 1
        max_seq = 1

        #sort arr
        nums.sort()

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]: #we found a duplicate
                continue
            if nums[i+1] == nums[i]+1:
                curr_seq+=1
                max_seq = max(max_seq, curr_seq)
            else:
                curr_seq = 1

        return max_seq 