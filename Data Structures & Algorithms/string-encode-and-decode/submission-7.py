class Solution:

    def encode(self, strs: List[str]) -> str:
        #print(strs)
        encoded = ""
        for i in range(len(strs)):
            encoded += str(len(strs[i])) + "#" + strs[i]
        
        return encoded
    def decode(self, s: str) -> List[str]:
        #print(s)
        res = []

        i = 0 
        
        while i < len(s):
            #print(i, res)
            number = ""
            while s[i].isdigit():
                number += s[i]
                i+=1
            
            number = int(number) + 1

            curr = ""

            for j in range(i+1, i+number):
                curr += s[j]
            
            res.append(curr)

            i = i+number
        
        return res

