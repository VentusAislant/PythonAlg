class Solution:
    def simplifyPath(self, path: str) -> str:
        path_lst = path.strip().split('/')
        stack = []
        for p in path_lst:
            if p == '' or p == '.':
                continue

            if p == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append('/' + p)
        if not stack:
            return '/'
        else:
            return ''.join(stack).strip()




if __name__ == '__main__':
    cases = [
        ("/home/", "/home"),
        ("/home//foo/", "/home/foo"),
        ("/home/user/Documents/../Pictures", "/home/user/Pictures"),
        ("/../", "/")
    ]
    solution = Solution()
    for case in cases:
        res = solution.simplifyPath(*case[:-1])
        print(res, case[-1])
