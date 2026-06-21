def solve(n: int, s:str) -> str:
    """
    dp[i][j] 以 s[i:j+1] 是否是回文串

    1. 当前长度为 1 (i==j): dp[i][j] = True
    2. 当前长度为 2 (j-i==1): dp[i][j] = s[i]==s[j]
    3. 当前长度为 3 (j-i==2): dp[i][j] = s[i]==s[j]
    4. 当前长度为 4 (j-i==4): dp[i][j] = s[i]==s[j] and dp[i+1][j-1]
    ...

    所以
        if j-i == 0:
            dp[i][j] = True
        elif j-i <= 2:
            dp[i][j] = s[i] == s[j]
        else:
            dp[i][j] = s[i]==s[j] and dp[i+1][j-1]

    注意 i需要逆向遍历，j需要正向，因为 i 用到了 i+1
    """
    dp = [[False for _ in range(n)] for _ in range(n)]
    max_len = 0
    start_pos = -1
    for i in range(n-1, -1, -1):
        for j in range(i, n):
            if j - i == 0:
                dp[i][j] = True
            elif j - i <= 2:
                dp[i][j] = s[i] == s[j]
            else:
                dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]

            if dp[i][j] and j-i+1 > max_len:
                max_len = j-i+1
                start_pos = i

    return s[start_pos:start_pos+max_len]

if __name__ == '__main__':
    s = input().strip()
    res = solve(len(s), s)
    print(res)