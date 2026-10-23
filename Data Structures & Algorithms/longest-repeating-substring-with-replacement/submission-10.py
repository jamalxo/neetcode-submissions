class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        l = 0
        r = 0
        max_window = 0

        for r in range(len(s)):
            c = s[r]
            counts[c] = counts.get(c, 0) + 1

            maxf = max(counts.values())

            while (r-l+1-maxf) > k: # 6-4 > 1
                removing = s[l]
                l += 1
                counts[removing] -= 1

            max_window = max(max_window, r-l+1)

        return max_window


