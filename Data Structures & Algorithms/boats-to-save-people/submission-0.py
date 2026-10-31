class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)


        l = 0
        r = len(people)-1

        count = 0

        while l <= r:
            print(l,r)
            if people[l] + people[r] <= limit or l == r:
                print("one")
                count += 1
                l +=1
                r -=1
                continue
            elif people[r] > people[l]:
                print("two")
                r -=1
                count +=1
                continue
            else:
                print("three")
                l+=1
                count+=1
                continue

        return count