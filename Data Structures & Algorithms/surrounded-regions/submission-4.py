class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(i, j, seen):
            outside = i < 0 or j < 0 or i >= len(board) or j >= len(board[0])
            if outside or (i,j) in seen or board[i][j] == 'X' or board[i][j] == 'T':
                return
            
            if board[i][j] == 'O':
                seen.add((i,j))
                board[i][j] = 'T'

            dfs(i+1, j, seen)
            dfs(i-1, j, seen)
            dfs(i, j+1, seen)
            dfs(i, j-1, seen)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                is_border = i == 0 or j == 0 or i == len(board)-1 or j == len(board[0])-1
                if board[i][j] == 'O' and is_border:
                    dfs(i, j, set())

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                            
        
        
