class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count = {}

        for word in s1.split(' ') + s2.split(' '):
            count[word] = count.get(word, 0) + 1
    

        return [k for k,v in count.items() if v == 1]
