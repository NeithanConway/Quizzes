# Given an array of integers nums sorted in ascending order, f
# ind the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# Follow up: Could you write an algorithm with O(log n) runtime complexity?
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        return [
            self.binarySearch(nums, target, True),
            self.binarySearch(nums, target, False),
        ]

    def binarySearch(self, arr: List[int], target: int, first: bool) -> int:
        min = 0
        max = len(arr) - 1
        mid = 0
        ret = -1
        while min <= max:
            mid = (min + max) // 2

            if arr[mid] == target:
                ret = mid
                if first:
                    max = mid - 1
                else:
                    min = mid + 1
            elif arr[mid] < target:
                min = mid + 1
            else:
                max = mid - 1

        return ret


print(Solution().searchRange([1, 2, 2, 2, 2, 3, 4], 2))
print(Solution().searchRange([1, 2, 2, 2, 2, 3, 4], 1))
print(Solution().searchRange([1, 2, 2, 3, 4], 2))
