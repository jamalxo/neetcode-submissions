class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1

        result = []

        while l < r:

            if numbers[l] + numbers[r] == target:
                result = [l + 1, r + 1]
                break
            if numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l +=1
        
        return result