class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0] * len(height)

        biggest_left = 0

        for i in range(len(height)):
            biggest_left = max(biggest_left, height[i])
            left_max[i] = biggest_left
        
        biggest_right = 0

        right_max = [0] * len(height)

        for i in range(len(height) -1, -1, -1):
            
            biggest_right = max(biggest_right, height[i])
            right_max[i] = biggest_right



        ## diff
        diff = [0] * len(height)

        for i in range(len(height)):
            diff[i] = min(left_max[i], right_max[i])

        ## res
        res = [0] * len(height)

        for i in range(len(height)):
            res[i] = diff[i] - height[i]
        
        return sum(res)