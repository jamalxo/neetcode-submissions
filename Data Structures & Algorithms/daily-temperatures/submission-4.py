class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = temperatures
        res = [0] * len(temp)

        mono = []

        for i in range(len(temp)):
            
            new = (temp[i], i)
            while mono and mono[-1][0] < new[0]:
                mono_t, mono_i = mono.pop()
                res[mono_i] = i - mono_i
            mono.append(new)
        
        return res