class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # rectangle = how many consecutive + max height of tiniest
        res = 0

        mono = []

        for i in range(len(heights)):
            h = heights[i]
            start = i
            while mono and mono[-1][1] > h:
                index, popped_height = mono.pop()
                res = max(res, popped_height* (i - index))
                start = index
            mono.append((start, h))
        
        print(mono)

        while mono:
            index, height = mono.pop()
            res = max(res, height * (len(heights) - index))

        return res