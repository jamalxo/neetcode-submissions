class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.pacific = set()
        self.atlantic = set()

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if j == 0 or i == 0:
                    self.pacific.add((i,j))
                if j == len(heights[0])-1 or i == len(heights)-1:
                    self.atlantic.add((i,j))

        def dfs(i, j, prev, ocean):
            
            outside = i < 0 or i >= len(heights) or j < 0 or j >= len(heights[0])
            if outside or (i,j) in ocean:
                return
            if prev and heights[i][j] < prev:
                return
            value = (i,j)
            ocean.add(value)
            prev_height = heights[i][j]
            dfs(i+1, j, prev_height, ocean)
            dfs(i-1, j, prev_height, ocean)
            dfs(i, j+1, prev_height, ocean)
            dfs(i, j-1, prev_height, ocean)

        new_pacific = set()
        new_atlantic = set()
        # dfs pacific
        for item in list(self.pacific):
            dfs(item[0], item[1], None, new_pacific)
        # dfs atlantic
        for item in list(self.atlantic):
            dfs(item[0], item[1], None, new_atlantic)


        return list(new_pacific & new_atlantic)