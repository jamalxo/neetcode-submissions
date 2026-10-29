from collections import deque
class Solution:

    def atMostOne(self, word1, word2):
        diff = 0
    
        for i, c in enumerate(word1):
            if c != word2[i]:
                diff += 1

        return diff == 1

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        counter = 1
        q = deque()
        q.append(beginWord)
        seen = set()

        while q:
            for _ in range(len(q)):
                popped = q.popleft()

                if popped == endWord:
                    return counter

                for word in wordList:
                    if self.atMostOne(popped, word) and popped != word and word not in seen:
                        q.append(word)
                        seen.add(word)
            counter += 1
        return 0