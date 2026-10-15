class Solution:
    def build_char_by_count(self, string):
        char_by_count = {}
        for i in range(len(string)):
            char_by_count[string[i]] = char_by_count.get(string[i], 0) + 1
        return char_by_count

    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        s1_dict = self.build_char_by_count(s1)

        window_string_dict = None

        for i in range(len(s2) - window + 1):
            if not window_string_dict:
                sub = s2[i:i+window]
                window_string_dict = self.build_char_by_count(sub)
            else:
                window_string_dict[s2[i-1]] -= 1
                if window_string_dict[s2[i-1]] == 0:
                    del window_string_dict[s2[i-1]]
                window_string_dict[s2[i+window-1]] = window_string_dict.get(s2[i+window-1], 0) + 1

            # now check if they are a perm
            if window_string_dict == s1_dict:
                return True
        
        return False