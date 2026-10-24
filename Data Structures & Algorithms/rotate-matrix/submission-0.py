class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        ## reverse order of rows
        l = 0
        r = len(matrix)-1

        while l<r:
            temp = matrix[l]
            matrix[l] = matrix[r]
            matrix[r] = temp
            l+=1
            r-=1
        
        print (matrix)
        
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix[0])):
                temp = matrix[i][j] 
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        
        



