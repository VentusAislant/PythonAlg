from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p, q = list1, list2
        head = None
        cur_node = head
        while p and q:
            print(p.val, q.val)
            if p.val < q.val:
                cur_val = p.val
                p = p.next
            else:
                cur_val = q.val
                q = q.next

            if head is None:
                head = ListNode(cur_val)
                cur_node = head
            else:
                cur_node.next = ListNode(cur_val)
                cur_node = cur_node.next

        while p:
            if head is None:
                head = ListNode(p.val)
                cur_node = head
            else:
                cur_node.next = ListNode(p.val)
                cur_node = cur_node.next
            p = p.next

        while q:
            if head is None:
                head = ListNode(q.val)
                cur_node = head
            else:
                cur_node.next = ListNode(q.val)
                cur_node = cur_node.next
            q = q.next

        return head


def construct_linked_list(lst: List[int]) -> Optional[ListNode]:
    if len(lst) == 0: return None
    head = ListNode(lst[0])
    cur_node = head
    for val in lst[1:]:
        cur_node.next = ListNode(val)
        cur_node = cur_node.next
    return head


def get_linked_list(head):
    cur_node = head
    res = []
    while cur_node:
        res.append(cur_node.val)
        cur_node = cur_node.next
    return res


if __name__ == '__main__':
    cases = [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
    ]
    solution = Solution()
    for case in cases:
        list1 = construct_linked_list(case[0])
        list2 = construct_linked_list(case[1])
        print(get_linked_list(list1), get_linked_list(list2))
        res = get_linked_list(solution.mergeTwoLists(list1, list2))
        print(res, case[-1])
