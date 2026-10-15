class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) -1

        if target < matrix[0][0]:
            return False
        
        skip_first_search = False

        middle = 0

        if target > matrix[-1][0]:
            skip_first_search = True
            middle = len(matrix) -1

        while l <= r and  not skip_first_search:
            middle = (r + l) // 2

            if matrix[middle][0] < target:
                l = middle + 1
            elif matrix[middle][0] > target:
                r = middle - 1
            else:
                return True
        
        row_to_check = r
        l = 0
        r = len(matrix[0])-1

        while l <= r:
            temp_middle = (r + l) // 2
            
            if matrix[row_to_check][temp_middle] < target:
                l = temp_middle + 1
            elif matrix[row_to_check][temp_middle] > target:
                r = temp_middle - 1
            else:
                return True
        
        return False