# Given an arbitrary ransom note string and another string containing letters
# from all the magazines, write a function that will return true if the ransom
# note can be constructed from the magazines ; otherwise, it will return false.

# Each letter in the magazine string can only be used once in your ransom note.

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        for letter in ransomNote:
            if letter in magazine:
                magazine = magazine.replace(letter, "", 1)
            else:
                return False

        return True

    def canConstructFaster(self, ransomNote: str, magazine: str) -> bool:
        magazineLetters = defaultdict(int)

        for letter in magazine:
            magazineLetters[letter] += 1

        for letter in ransomNote:
            if magazineLetters[letter] <= 0:
                return False
            magazineLetters[letter] -= 1

        return True


print(Solution().canConstruct("a", "b"))
print(Solution().canConstructFaster("a", "b"))
# False
print(Solution().canConstruct("a", "ab"))
print(Solution().canConstructFaster("a", "ab"))
# True
print(Solution().canConstruct("aa", "ab"))
print(Solution().canConstructFaster("aa", "ab"))
# False
print(Solution().canConstruct("aa", "aab"))
print(Solution().canConstructFaster("aa", "aab"))
# True
print(Solution().canConstruct("aba", "ab"))
print(Solution().canConstructFaster("aba", "ab"))
# False
