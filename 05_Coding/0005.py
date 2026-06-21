def is_hui(s):
    l, r = 0, len(s)-1
    while l < r:
        if s[l] != s[r]:
            return False

        l += 1
        r -= 1
    return True

def solve(n: int, k: int, s: str) -> str:
    t = ""
    for i in range(0, n, k):
        cur_str = s[i:min(i+k, n)]
        if is_hui(cur_str):
            t = cur_str + t
        else:
            t = t + cur_str

    return t


if __name__ == '__main__':
    n, k = tuple(map(int, input().split()))
    s = input().strip()
    res = solve(n, k, s)
    print(res)