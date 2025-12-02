from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        lst = self.get_linked_list(head)
        i, j = left - 1, right - 1
        while i < j:
            lst[j], lst[i] = lst[i], lst[j]
            i += 1
            j -= 1
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
        ([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5]),
        ([5], 1, 1, [5]),
    ]
    solution = Solution()
    for case in cases:
        linked_lst = solution.construct_linked_list(case[0])
        print(solution.get_linked_list(linked_lst))
        res = solution.get_linked_list(solution.reverseBetween(linked_lst, case[1], case[2]))
        print(res, case[-1])
