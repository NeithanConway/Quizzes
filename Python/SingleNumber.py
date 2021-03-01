# Given a non-empty array of integers nums, every element appears
# twice except for one. Find that single one.

# Follow up: Could you implement a solution with a linear runtime
# complexity and without using extra memory?
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ret = 0
        for n in nums:
            ret ^= n
        return ret


print(Solution().singleNumber([4, 1, 2, 1, 2]))
