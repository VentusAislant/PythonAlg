def solve(n: int, nums: list[int]) -> int:
    """
    1 2 -1 3 4 -> 9

    dp[i]: 表示 以第 i 个数结尾的的最大连续和

    if nums[i] < 0:
        if dp[i-1] + nums[i] >= 0:
            dp[i] = dp[i-1] + nums[i]
        else:
            dp[i] = 0
    else:
        dp[i] = dp[i-1] + nums[i]
    """
    dp = [0] * n
    dp[0] = nums[0]
    for i in range(1, n):
        dp[i] = max(dp[i - 1] + nums[i], nums[i])

    return max(dp)


if __name__ == '__main__':
    nums = list(map(int, input().strip().split(',')))
    res = solve(len(nums), nums)
    print(res)
