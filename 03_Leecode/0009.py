class Solution:
    def isPalindrome(self, x: int) -> bool:
        lst = list(str(x))
        i, j = 0, len(lst) - 1
        while i < j:
            if lst[i] != lst[j]:
                return False
            i += 1
            j -= 1
        return True

    def isPalindrome2(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
