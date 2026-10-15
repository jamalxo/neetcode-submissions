class Solution:
    def get_max_map(self, map):
        return max(map.values())
    
    def characterReplacement(self, s: str, k: int) -> int:
        seen_map = {}

        left = 0
        right = 0

        longest = 0
        for right in range(len(s)):
            c = s[right]
            seen_map[c] = seen_map.get(c, 0) + 1 

            maxf = self.get_max_map(seen_map)
            
            # is window valid?
            while (right - left + 1 -  maxf) > k:
                removing_c = s[left]
                seen_map[removing_c] -= 1
                left += 1
            longest = max(longest, right - left + 1)

        return longest


