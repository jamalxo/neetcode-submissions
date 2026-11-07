class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append((price, 1))
            return 1

        #(price, consecutive days)
        prev = self.stack[-1]
        curr = (price, 1)
        if curr[0] >= prev[0]:
            while len(self.stack) > 0 and prev[0] <= curr[0]:
                self.stack.pop()
                curr = (curr[0], curr[1]+prev[1])
                prev = self.stack[-1] if len(self.stack) > 0 else None
                
            self.stack.append(curr)
        else:
            self.stack.append(curr)

        return self.stack[-1][1]





# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)