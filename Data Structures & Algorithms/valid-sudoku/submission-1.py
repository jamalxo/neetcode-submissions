class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:        
        # rows duplicated
        for i in range(len(board)):
            seen = set()
            for j in range(len(board[0])):
                if board[i][j].isdigit():
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
        
        # col duplicated
        for j in range(len(board[0])):
            seen = set()
            for i in range(len(board)):
                if board[i][j].isdigit():
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                seen = set()
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        if board[k][l].isdigit():
                            if board[k][l] in seen:
                                return False
                            seen.add(board[k][l])
        return True
