# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

# You can return the answer in any order.
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i1, n1 in enumerate(nums):
            for i2, n2 in enumerate(hash):
                if n1 + n2 == target:
                    return [i1, hash[n2]]
            hash[n1] = i1

        return []


print(Solution().twoSum([1, 4, 8, 6], 10))
print(Solution().twoSum([1, 3, 8, 6], 10))
