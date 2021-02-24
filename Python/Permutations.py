# Given an array nums of distinct integers,
# return all the possible permutations. You can return the answer in any order.
# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.permuteHelper([], nums, len(nums))

    def permuteHelper(
        self, ret: List[List[int]], nums: List[int], last_elem: int
    ) -> List[List[int]]:

        ret.append(nums[:])

        if last_elem <= 1:
            return ret

        for j in range(last_elem - 1):
            next_last_elem = last_elem - j - 1
            for i in range(next_last_elem):
                next_nums = self.swapPositions(nums[:], next_last_elem, i)
                ret = self.permuteHelper(ret, next_nums, next_last_elem)
        return ret

    def swapPositions(self, list, pos1, pos2):
        list[pos1], list[pos2] = list[pos2], list[pos1]
        return list


print(Solution().permute([1, 2, 3]))
