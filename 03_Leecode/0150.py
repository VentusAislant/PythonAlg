from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        od_stack = []
        preference = {
            '+': 1, '-': 1, '*': 2, '/': 2
        }
        print(tokens)
        for token in tokens:
            if token not in preference:
                od_stack.append(int(token))
            else:
                b = od_stack.pop()
                a = od_stack.pop()
                if token == '+':
                    res = a + b
                elif token == '-':
                    res = a - b
                elif token == '*':
                    res = a * b
                else:
                    res = int(a / b)
                od_stack.append(res)

        return od_stack[-1] if od_stack else 0


if __name__ == '__main__':
    cases = [
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
    ]
    solution = Solution()
    for case in cases:
        res = solution.evalRPN(*case[:-1])
        print(res, case[-1])
