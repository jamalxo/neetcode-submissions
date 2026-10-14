class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)

        longest = 0

        for val in set_nums:
            # is start of sequence?
            if val-1 in set_nums:
                continue
            else:
                count = 1
                current = val
                while True:
                    if current+1 in set_nums:
                        count += 1
                        current +=1
                    else:
                        break
                longest = max(longest, count)
        
        return longest