class Solution:
    def check_word(self, one, two, order_map):
        i = 0
        j = 0
        for i in range(len(one)):
            pos1 = order_map[one[i]]
            if i >= len(two):
                return False
            pos2 = order_map[two[i]]
            if pos2 == pos1:
                continue
            elif pos2 < pos1:
                return False
            else:
                return True
        return True

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {}

        for i in range(len(order)):
            order_map[order[i]] = i
        
        res = True

        if len(words) < 1:
            return res

        for i in range(1, len(words)):
            if not self.check_word(words[i-1], words[i], order_map):
                return False
        
        return True