from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)  # 如果不为None，则表示p或q在左子树
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            # 一个在左子树，一个在右子树
            return root
        return left if left else right

def construct_tree(level_order):
    queue = deque()
    root = TreeNode(level_order[0])
    queue.append(root)
    i = 1
    while queue:
        node = queue.popleft()
        if i < len(level_order):
            node.left = TreeNode(level_order[i]) if level_order[i] is not None else None
            queue.append(node.left)
            i += 1
        if i < len(level_order):
            node.right = TreeNode(level_order[i]) if level_order[i] is not None else None
            queue.append(node.right)
            i += 1
    return root

def level_order(root: TreeNode) -> List[Optional[int]]:
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
        ([3,5,1,6,2,0,8,None,None,7,4], 5, 1, 3),
    ]
    for case in cases:
        tree = construct_tree(case[0])
        res = solution.lowestCommonAncestor(tree, case[1], case[2])
        print(res, case[-1])
