class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        self.cache = {}
        self.works = False

        def dfs(i, j):
            #print(i,j)
            current = len(i) + len(j)
            if current >= len(s3) and (i != s1 or j != s2):
                return 0
            if current == len(s3) and i == s1 and j == s2:
                self.works = True
                return 1
            if (i,j) in self.cache:
                return self.cache[(i,j)]


            # add to i
            one = 0
            if len(s1) > len(i) and s1[len(i)] == s3[current]:
                one = dfs(i+s3[current], j)

            # add to j
            two = 0
            if len(s2) > len(j) and s2[len(j)] == s3[current]:
                two = dfs(i, j+s3[current])

            self.cache[(i,j)] = one + two
            return self.cache[(i,j)]

        dfs("","")
        print(self.cache)


        return self.works