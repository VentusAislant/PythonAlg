from copy import deepcopy
from typing import List, Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        return deepcopy(head) if head else None


def construct_from_lst(lst):
    link_lst = [item[0] for item in lst]
    id2node = {}
    head = Node(link_lst[0])
    id2node[0] = head
    cur = head
    for i in range(1, len(link_lst)):
        cur.next = Node(link_lst[i])
        id2node[i] = cur
        cur = cur.next

    cur = head
    for i in range(lst):
        random_idx = lst[i][1]
        if random_idx is None:
            cur.random = None
        else:
            cur.random = id2node[random_idx]
        cur = cur.next
    return head


if __name__ == '__main__':
    cases = [
        (
            [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
            [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
        ),
        (
            [[1, 1], [2, 1]],
            [[1, 1], [2, 1]]
        ),
        (
            [[3, None], [3, 0], [3, None]],
            [[3, None], [3, 0], [3, None]]
        ),
    ]
    solution = Solution()
    for case in cases:
        l1 = construct_from_lst(case[0])
        res = solution.copyRandomList(l1)
        print(res, case[-1])
