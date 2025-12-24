class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        最简单的思路就是枚举所有的两数和，然后判断哪一组数满足条件，时间复杂度 O(N^2)
        上述方法可以简化为两步，第一步枚举每一个数 x, 第二步，寻找数组中是否存在 target - x

        关键可以优化的地方是寻找数组中是否存在 target - x
        我们可以先用一个哈希表来存储所有的元素，然后枚举每一个数x,直接从哈希表中查看是否存在 targe-x 即可，
        而且得保证这个 target-x 的索引不是自己（否则就不是两个数了）

        时间复杂度 O(N)
        空间复杂度 O(N)
        """
        num2idx = {num: i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            complete = target - num
            if complete in num2idx and num2idx[complete] != i:
                return [i, num2idx[complete]]
        return []

    def twoSumV1(self, nums: list[int], target: int) -> list[int]:
        """
        排序 + 双指针
            先将数组升序排列, 但是得记录原来的下标，使用左右指针，来寻找这两个数的下标

        时间复杂度 O(N*logN)
        空间复杂度 O(N)
        """
        nums = [(i, num) for i, num in enumerate(nums)]
        nums.sort(key=lambda x: x[1])
        left, right = 0, len(nums) - 1
        while left < right:
            cur_sum = nums[left][1] + nums[right][1]
            if cur_sum == target:
                return [nums[left][0], nums[right][0]]
            elif cur_sum < target:
                left += 1
            else:
                right -= 1
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
