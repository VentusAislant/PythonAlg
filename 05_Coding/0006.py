from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)

def solve(n, Q, edge_nodes, a_lst, b_lst) -> int:
    graph = defaultdict(list)

    for i, fi in enumerate(edge_nodes):
        graph[fi].append(i+2)

    # 记录每个结点而子树的叶子结点数
    leaf = [0] * (n+1)
    def dfs(node):
        # 当前是叶子结点
        if node != 1 and len(graph[node]) == 0:
            leaf[node] = 1
            return

        # 否则统计叶子结点数
        total = 0
        for v in graph[node]:
            dfs(v)
            total += leaf[v]
        leaf[node] = total
    dfs(1)

    res = 0
    for a, b in zip(a_lst, b_lst):
        res ^= leaf[a] * leaf[b]

    return res


if __name__ == '__main__':
    n, Q = tuple(map(int, input().split()))
    edge_nodes = list(map(int, input().split()))
    a_lst = list(map(int, input().split()))
    b_lst = list(map(int, input().split()))
    res = solve(n, Q, edge_nodes, a_lst, b_lst)
    print(res)