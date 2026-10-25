class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        seen = set()

        longest = 0

        while r < len(s):
            #if s[r] not in seen:
            #    seen.add(s[r])
            #    r+=1
            #    longest = max(longest, r-l)
            #else:
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            r+=1
            longest = max(longest, r-l)

        return longest
            