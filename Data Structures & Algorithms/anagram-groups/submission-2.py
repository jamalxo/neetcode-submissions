class Solution:
    def isAnagram(self, one, two):
        c1 = Counter(one)
        c2 = Counter(two)
        return c1 == c2

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        
        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            
            res.setdefault(key, []).append(strs[i])

        return list(res.values())