class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows
        for row in board:
            seen = set()
            for value in row:
                if value in seen:
                    return False
                elif value == ".":
                    continue
                else:
                    seen.add(value)
        
        # cols
        for i in range(len(board)):
            seen = set()
            for j in range(len(board)):
                if board[j][i] in seen:
                    return False
                elif board[j][i] == ".":
                    continue
                else:
                    seen.add(board[j][i])

        # grid
        for bow_row in range(3):
            for bow_col in range(3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        val = board[bow_row*3 + i][bow_col*3 + j]
                        if val in seen:
                            return False
                        elif val == ".":
                            continue
                        else:
                            seen.add(val)

        return True
            