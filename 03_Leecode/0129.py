from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        nums = []
        # 层序遍历思想
        self.preorder(root, cur_path=[], res=nums)
        return sum(nums)

    def compute_sum(self, path_vals):
        base = 1
        res = 0
        for num in path_vals[::-1]:
            res += num * base
            base *= 10
        return res

    def preorder(self, node, cur_path, res):
        cur_path.append(node.val)
        if node.left is None and node.right is None:
            res.append(self.compute_sum(cur_path))

        if node.left:
            self.preorder(node.left, cur_path=cur_path, res=res)
            cur_path.pop()

        if node.right:
            self.preorder(node.right, cur_path=cur_path, res=res)
            cur_path.pop()


def construct_tree(level_order):
    if not level_order: return None
    root = TreeNode(level_order[0])
    queue = deque([root])
    i = 1
    while queue and i < len(level_order):
        node = queue.popleft()
        if i < len(level_order) and level_order[i] is not None:
            node.left = TreeNode(level_order[i])
            i += 1
            queue.append(node.left)

        if i < len(level_order) and level_order[i] is not None:
            node.right = TreeNode(level_order[i])
            i += 1
            queue.append(node.right)
    return root


def level_order(root):
    queue = deque()
    queue.append(root)
    res = []
    while queue:
        node = queue.popleft()
        res.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return res


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([1, 2, 3], 25),
        ([4, 9, 0, 5, 1], 1026)
    ]
    for case in cases:
        root = construct_tree(case[0])
        print(level_order(root))
        res = solution.sumNumbers(root)
        print(res, case[-1])
