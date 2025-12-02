from typing import List, Optional
from collections import Counter


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        lst = self.get_linked_list(head)
        k = k % len(lst) if len(lst) > 0 else 0
        lst.reverse()
        lst[:k] = lst[:k][::-1]
        lst[k:] = lst[k:][::-1]
        return self.construct_linked_list(lst)

    def construct_linked_list(self, lst: List[int]) -> Optional[ListNode]:
        if len(lst) == 0: return None
        head = ListNode(lst[0])
        cur_node = head
        for val in lst[1:]:
            cur_node.next = ListNode(val)
            cur_node = cur_node.next
        return head

    def get_linked_list(self, head):
        cur_node = head
        res = []
        while cur_node:
            res.append(cur_node.val)
            cur_node = cur_node.next
        return res


if __name__ == '__main__':
    cases = [
        ([1,2,3,4,5],2, [4,5,1,2,3]),
    ]
    solution = Solution()
    for case in cases:
        linked_lst = solution.construct_linked_list(case[0])
        print(solution.get_linked_list(linked_lst))
        res = solution.get_linked_list(solution.rotateRight(linked_lst, case[1]))
        print(res, case[-1])
