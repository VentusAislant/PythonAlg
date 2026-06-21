def can_move(x, y, p, q, nums) -> bool:
    """
    起点 (x,y), 终点 (p,q), 行走的数组 nums = [a1, a2, ..., an]
    每次行走到 x+l, y+r, 满足 |l|+|r|=a

    看似是回溯，实际上是数学+贪心

    我有 n 个数，每个数可以分给 x 和 y, 最终要拼出来 dx 和 dy
    必须满足|dx| + |dy| <= sum(a)， 如若不然一直朝着目标走也走不到，肯定最后无法到达
    必须满足 sum(a) - |dx| - |dy| 是偶数， 否则一定到不了
        因为每个 ai 必须全部用掉，假设多出来的距离为 extra = sum(a) - |dx| - |dy|
        就必须吧 extra 消耗掉，可以通过折返走的方式 +1 再 -1 如果是奇数肯定无法满足，所以一定不行
    """

    sum_num = sum(nums)
    dx, dy = abs(p - x), abs(q - y)
    if sum_num - dx - dy < 0:
        return False
    elif (sum_num - dx - dy) % 2 == 1:
        return False

    return True

if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        nums = list(map(int, input().strip().split()))
        x,y,p,q = tuple(map(int, input().strip().split()))
        if can_move(x, y, p, q, nums):
            print("YES")
        else:
            print("NO")