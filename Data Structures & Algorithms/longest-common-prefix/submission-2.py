class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        how_many = 0

        first = strs[0]

        for i in range(len(first)):
            c = first[i]
            for word in strs:
                if word == "":
                    return ""
                if i >= len(word) or word[i] != c:
                    return first[:how_many]
                
            how_many += 1
        
        return first[:how_many]