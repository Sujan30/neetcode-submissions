class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #move pointer based off which one has the lower height


        l = 0
        r = len(heights)-1

        max_area = -1
        while l<r:
            curr_area = min(heights[l], heights[r]) * (r-l)
            max_area = max(max_area, curr_area)
            
            #trying to maximize height
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return max_area
        