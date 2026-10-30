class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        self.cache = {}

        def dfs(i, j):
            current = len(i) + len(j)
            if current >= len(s3) and (i != s1 or j != s2):
                return False
            if current == len(s3) and i == s1 and j == s2:
                return True
            if (i,j) in self.cache:
                return self.cache[(i,j)]


            # add to i
            one = False
            if len(s1) > len(i) and s1[len(i)] == s3[current]:
                one = dfs(i+s3[current], j)

            # add to j
            two = False
            if len(s2) > len(j) and s2[len(j)] == s3[current]:
                two = dfs(i, j+s3[current])

            self.cache[(i,j)] = one or two
            return self.cache[(i,j)]

        return dfs("","")