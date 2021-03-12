# There are a total of numCourses courses you have to take, l
# abeled from 0 to numCourses - 1. You are given an array
# prerequisites where prerequisites[i] = [ai, bi] indicates that you
# must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_table = {}
        cash_table = {}
        for n in range(numCourses):
            course_table[n] = []

        for preq in prerequisites:
            course_table[preq[0]].append(preq[1])

        for course in course_table:
            if not self.canBeFinishedCourse(cash_table, course, course_table):
                return False

        return True

    def canBeFinishedCourse(self, cash_table, course, course_table) -> bool:
        if course in cash_table:
            return cash_table[course]

        cash_table[course] = False

        for preq in course_table[course]:
            if not self.canBeFinishedCourse(cash_table, preq, course_table):
                return False

        cash_table[course] = True

        return True


print(Solution().canFinish(2, [[1, 0], [0, 1]]))
print(Solution().canFinish(2, [[1, 0]]))
print(Solution().canFinish(3, [[1, 0], [1, 2], [0, 1]]))
print(Solution().canFinish(4, [[2, 0], [1, 0], [3, 1], [3, 2], [1, 3]]))
