class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []

        """
        i = middle pointer (parition)
        l = left of i
        r = right of i

        """
        nums = sorted(nums)
        
        for i in range(len(nums)):
            j = i+1
            r = len(nums)-1
            while j<r:
                curr = -1*(nums[j] + nums[r])
                if curr == nums[i]:
                    ans.append([nums[i],nums[j], nums[r]])
                    j+=1
                elif curr > nums[i]:
                    j+=1
                else:
                    r-=1
        return list(set(tuple(i) for i in ans))









