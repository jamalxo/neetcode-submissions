class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)

        #print(c)

        res = []
        curr = 0

        #print(c)

        for key,v in sorted(c.items(), key=lambda x: x[1], reverse=True):
            #print(curr, k)
            if curr < k:
                res.append(key)
            curr+=1
        return res