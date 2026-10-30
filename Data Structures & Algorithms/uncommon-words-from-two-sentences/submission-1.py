class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        set_a = set()
        set_b = set()

        dict_a = {}
        dict_b = {}

        for word in s1.split(' '):
            dict_a[word] = dict_a.get(word, 0) + 1


        for word in s2.split(' '):
            dict_b[word] = dict_b.get(word, 0) + 1


        for k,v in dict_a.items():
            if v == 1:
                set_a.add(k)

        for k,v in dict_b.items():
            if v == 1:
                set_b.add(k)
        print(dict_a)
        print(dict_b)

        return list(set_a.difference(set(s2.split(' ')))) + list(set_b.difference(set(s1.split(' '))))
