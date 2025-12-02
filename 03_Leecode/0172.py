import math

class Solution:
    def trailingZeroes(self, n: int) -> int:
        num = math.factorial(n)
        cnt = 0
        while num > 0:
            last_digit = num % 10
            if last_digit == 0:
                cnt += 1
            else:
                break
            num //= 10
        return cnt