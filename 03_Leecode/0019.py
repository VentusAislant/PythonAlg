from typing import List, Optional
from collections import Counter


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = self.get_linked_list(head)
        counter = Counter(lst)
        lst = list(k for k, v in counter.items() if v == 1)
        lst.sort()
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
        ([1, 1, 1, 2, 3], [2, 3]),
    ]
    solution = Solution()
    for case in cases:
        linked_lst = solution.construct_linked_list(case[0])
        print(solution.get_linked_list(linked_lst))
        res = solution.get_linked_list(solution.deleteDuplicates(linked_lst))
        print(res, case[-1])
