class Solution:
    def build_char_by_count(self, string):
        char_by_count = {}
        for i in range(len(string)):
            char_by_count[string[i]] = char_by_count.get(string[i], 0) + 1
        return char_by_count

    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        s1_dict = self.build_char_by_count(s1)

        for i in range(len(s2)):
            sub = s2[i:i+window]
            
            window_string_dict = self.build_char_by_count(sub)

            # now check if they are a perm
            if window_string_dict == s1_dict:
                return True
        
        return False