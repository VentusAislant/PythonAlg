from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.get_num(l1)
        l2 = self.get_num(l2)
        num = l1 + l2
        return self.construct_from_num(num)

    def get_num(self, link_list: ListNode) -> Optional[int]:
        cur = link_list
        res = 0
        base = 1
        while cur:
            res += cur.val * base
            base *= 10
            cur = cur.next
        return res

    def construct_from_num(self, num):
        num_lst = []
        if num == 0: num_lst.append(0)
        while num > 0:
            num_lst.append(num % 10)
            num = num // 10

        head = ListNode(num_lst[0])
        cur = head
        for num in num_lst[1:]:
            cur.next = ListNode(num)
            cur = cur.next
        return head


def construct_linked_list(lst):
    head = ListNode(lst[0])
    cur = head
    for val in lst[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return head


if __name__ == '__main__':
    cases = [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
    ]
    solution = Solution()
    for case in cases:
        l1 = construct_linked_list(case[0])
        l2 = construct_linked_list(case[1])
        res = solution.addTwoNumbers(l1, l2)
        print(res, case[-1])
