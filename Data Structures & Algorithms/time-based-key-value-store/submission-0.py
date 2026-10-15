class TimeMap:

    def __init__(self):
        self.people = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.people.setdefault(key, []).append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        times = self.people.get(key, [])

        l = 0
        r = len(times) - 1

        while l <= r:
            middle = (l+r) // 2

            if times[middle][1] == timestamp:
                return times[middle][0]
            elif times[middle][1] < timestamp:
                l = middle + 1
            else:
                r = middle - 1

        return times[r][0] if r >= 0 else ""
        
