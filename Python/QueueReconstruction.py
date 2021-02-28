# You are given an array of people, people, which are the attributes of some people in
# a queue (not necessarily in order). Each people[i] = [hi, ki] represents the ith person
# of height hi with exactly ki other people in front who have a height greater than or equal to hi.

# Reconstruct and return the queue that is represented by the input array people.
# The returned queue should be formatted as an array queue, where queue[j] = [hj, kj]
# is the attributes of the jth person in the queue (queue[0] is the person at the front of the queue).
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=lambda human: (human[1], human[0]))
        sorted_people = []

        while people:
            high_counter = 0
            new_human = people.pop(0)
            for i, human in enumerate(sorted_people):
                if human[0] >= new_human[0]:
                    high_counter += 1
                if new_human[1] == high_counter:
                    if (
                        len(sorted_people) > i + 1
                        and sorted_people[i + 1][0] < new_human[0]
                    ):
                        continue
                    while i < len(sorted_people) - 1:
                        people.insert(0, sorted_people.pop())
                    break

            sorted_people.append(new_human)

        return sorted_people


people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
print(Solution().reconstructQueue(people))