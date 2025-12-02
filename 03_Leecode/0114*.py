from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        preorder_lst = []
        self.preorder(root, preorder_lst)
        for i in range(0, len(preorder_lst) - 1):
            preorder_lst[i].right = preorder_lst[i + 1]
            preorder_lst[i].left = None

    def preorder(self, node, store_lst):
        if not node:
            return None
        store_lst.append(node)
        self.preorder(node.left, store_lst)
        self.preorder(node.right, store_lst)


def construct_tree(level_order):
    if not level_order: return None
    root = TreeNode(level_order[0])
    queue = deque()
    queue.append(root)
    i = 1
    while queue and i < len(level_order):
        node = queue.popleft()
        if i < len(level_order):
            node.left = TreeNode(level_order[i]) if level_order[i] is not None else None
            i += 1
            queue.append(node.left)

        if i < len(level_order):
            node.right = TreeNode(level_order[i]) if level_order[i] is not None else None
            i += 1
            queue.append(node.right)
    return root


def level_order(root):
    queue = deque()
    queue.append(root)
    res = []
    while queue:
        node = queue.popleft()
        if node is not None:
            res.append(node.val)
            # 无论左右是否为 None，都入队
            queue.append(node.left)
            queue.append(node.right)
        else:
            res.append(None)

    # 去掉末尾多余的None
    while res and res[-1] is None:
        res.pop()
    return res


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([1, 2, 5, 3, 4, None, 6], [1, None, 2, None, 3, None, 4, None, 5, None, 6]),
        ([], []),
        ([0], [0])
    ]
    for case in cases:
        root = construct_tree(case[0])
        solution.flatten(root)
        print(level_order(root), case[-1])
