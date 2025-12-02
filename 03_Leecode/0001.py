from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {nums[i]: i for i in range(len(nums))}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_to_index and num_to_index[complement] != i:
                return [num_to_index[complement], i]

        return []


if __name__ == '__main__':
    cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ]
    solution = Solution()
    for case in cases:
        res = solution.twoSum(*case[:-1])
        print(res, case[-1])
