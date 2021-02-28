# Given an array nums with n objects colored red, white,
# or blue, sort them in-place so that objects of the same color
# are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red,
# white, and blue, respectively.
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero_idx = 0
        two_idx = len(nums) - 1
        idx = 0

        while idx <= two_idx:
            if nums[idx] == 0:
                nums[idx], nums[zero_idx] = nums[zero_idx], nums[idx]
                zero_idx += 1
                idx += 1
            elif nums[idx] == 2:
                nums[idx], nums[two_idx] = nums[two_idx], nums[idx]
                two_idx -= 1
            else:
                idx += 1


arr = [2, 0, 2, 1, 1, 0]
Solution().sortColors(arr)
print(arr)

arr = [1, 2, 0]
Solution().sortColors(arr)
print(arr)