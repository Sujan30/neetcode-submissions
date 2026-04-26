class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Brute Force O(n^2)
        
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
        """

        """

        3 cases:

        1. No zeroes
            take product of arr, and divide by nums[i]
        2. 1 zero
            take product of arr, if nums[i] != 0 return 0, else return product of arr
        3. more than 1 zero
            just return 0

        """
        product_arr = []
        product = 1
        zero_count = 0
        for n in nums:
            product*=n
            if n == 0:
                zero_count+=1
        #case 1
        if 0 not in nums:
            for num in nums:
                product_arr.append(product//num)
            return product_arr
        #case 2
        if zero_count == 1:
            product = 1
            for n in nums:
                if n != 0:
                    product*=n
            for n in nums:
                if n !=0:
                    product_arr.append(0)
                else:
                    product_arr.append(product)
            return product_arr
        else:
            for n in nums:
                product_arr.append(0)
            return product_arr

        
        
            
            
             
            
