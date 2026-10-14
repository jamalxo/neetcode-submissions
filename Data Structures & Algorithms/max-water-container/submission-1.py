class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1


        ## max water == max height * distance

        max_water = 0
        
        while l < r:
            print(r,l)
            max_water = max(min(heights[l], heights[r]) * (r-l), max_water)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_water
        