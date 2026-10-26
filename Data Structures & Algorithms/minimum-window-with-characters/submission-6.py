class Solution:
    def is_valid(self, map1, target):
        valid = True
        for k,v in target.items():
            if k in map1:
                if map1[k] < v:
                    valid = False
            else:
                valid = False
        return valid

    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0

        count = {}
        target_count = {}

        for c in t:
            target_count[c] = target_count.get(c, 0)+1

        min_string = 2**31
        min_str = ""
        best_l = None
        best_r = None
        have = 0
        need = len(target_count)

        while r < len(s) or have == need:
            if have == need:
                if r-l < min_string:
                    min_string = r-l
                    best_l, best_r = l, r
                c = s[l]
                count[c] -= 1
                if c in target_count and count[c] == target_count[c]-1:
                    have -= 1
                l+=1
            else:
                c = s[r]
                count[c] = count.get(c, 0)+1
                r+=1
                if c in target_count and count[c] == target_count[c]:
                    have += 1

        return s[best_l:best_r] if best_l or best_r else ""