class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        last_idx = -1
        product_arr = []
        product = 1
        for i in range(len(nums)):
            for j in range(0,i):
                product*=nums[j]
            for n in range(i+1, len(nums)):
                product*=nums[n]
            product_arr.append(product)
            product = 1
        return product_arr
            
