class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.res = False


        def dfs(i, j, curr):
            if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0:
                return
            if board[i][j] == "#":                       # already on this path
                return
            new_word = curr + board[i][j]
            if not word.startswith(new_word):            # wrong letter: stop
                return
            if new_word == word:                         # check right after adding
                self.res = True
                return
            temp = board[i][j]
            board[i][j] = '#'
            dfs(i+1, j, new_word)
            dfs(i, j+1, new_word)
            dfs(i-1, j, new_word)
            dfs(i, j-1, new_word)
            board[i][j] = temp


        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i,j,"")

        return self.res