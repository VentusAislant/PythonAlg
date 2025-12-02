from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder or not inorder:
            return None

        root = TreeNode(postorder[-1])
        idx = inorder.index(postorder[-1])
        root.right = self.buildTree(inorder[idx + 1:], postorder[idx:-1])
        root.left = self.buildTree(inorder[:idx], postorder[:idx])
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
        ([9, 3, 15, 20, 7], [9, 15, 7, 20, 3], [3, 9, 20, None, None, 15, 7]),
        ([-1], [-1], [-1])
    ]
    for case in cases:
        res = solution.buildTree(case[0], case[1])
        res = level_order(res)
        print(res, case[-1])
