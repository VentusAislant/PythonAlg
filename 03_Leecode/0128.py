class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """
        首先用一个哈希表 set 存储所有的元素
            枚举 nums 中的每一个数 x
            首先判断 x+1 是否在 set 中，如果在，可以继续判断 x+2 ...，同时记录右侧连续长度
            其次判断 x-1 是否在 set 中，如果在，可以继续判断 x-2 ...，同时记录左侧连续长度
            记录当前最长连续长度，开始下一个数
        时间复杂度 O(N)
        空间复杂度 O(N)
        """
        nums = set(nums)
        seen = set()
        max_len = 0
        for x in nums:
            if x in seen:
                continue

            right = x + 1
            right_len = 0
            while right in nums:
                right_len += 1
                seen.add(right)
                right = right + 1

            left = x - 1
            left_len = 0
            while left in nums:
                left_len += 1
                seen.add(left)
                left = left - 1

            max_len = max(max_len, right_len + left_len + 1)

        return max_len


if __name__ == '__main__':
    cases = [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([1, 0, 1, 2], 3),
    ]
    solution = Solution()
    for case in cases:
        res = solution.longestConsecutive(case[0])
        print(res, case[1])
