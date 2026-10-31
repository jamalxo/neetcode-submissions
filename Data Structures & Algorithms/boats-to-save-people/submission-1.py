class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)


        l = 0
        r = len(people)-1

        count = 0

        while l <= r:
            if people[l] + people[r] <= limit or l == r:
                count += 1
                l +=1
                r -=1
            elif people[r] > people[l]:
                r -=1
                count +=1
            else:
                l+=1
                count+=1
                continue

        return count