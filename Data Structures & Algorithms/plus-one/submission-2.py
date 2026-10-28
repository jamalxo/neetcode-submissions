from collections import deque

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        d = deque()

        carry_over = 1

        for i in range(len(digits)-1, -1, -1):
            new = digits[i] + carry_over
            left_over = new % 10
            carry_over = 1 if new == 10 else 0
            print(carry_over)
            d.appendleft(left_over)
        
        if carry_over == 1:
            d.appendleft(1)


        return list(d)
