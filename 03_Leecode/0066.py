from typing import *


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        i = len(digits) - 1
        while i >= 0:
            if i > 0 and digits[i] >= 10:
                digits[i] -= 10
                digits[i - 1] += 1
            elif i == 0 and digits[i] >= 10:
                digits[0] -= 10
                digits.insert(0, 1)
            else:
                break
            i -= 1
        return digits
