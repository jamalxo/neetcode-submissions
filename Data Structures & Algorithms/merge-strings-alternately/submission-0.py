class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0

        r = 0

        new = ""


        while l < len(word1) and r < len(word2):
            new += word1[l]
            new += word2[r]
            l+=1
            r+=1
        
        if l < len(word1):
            new += word1[l:]
        print(r)
        print(len(word2))
        if r < len(word2):
            print("adding")
            new += word2[r:]

        return new