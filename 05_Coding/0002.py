def solve(n, nums) -> int:
    """
    每次从右往左吃，更新，然后看多少次总条数没变
    """
    cnt = 0
    cur_len = -1
    last_len = n
    while cur_len != last_len:
        last_len = len(nums)
        new_nums = [nums[0]]
        for i in range(1, last_len):
            if nums[i] >= nums[i-1]:
                new_nums.append(nums[i])  # 吃不了，活下来
        cur_len = len(new_nums)
        nums = new_nums
        cnt +=1
    return cnt - 1

if __name__ == '__main__':
    n = int(input().strip())
    nums = list(map(int, input().strip().split()))
    res = solve(n, nums)
    print(res)