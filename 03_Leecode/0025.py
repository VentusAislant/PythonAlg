from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pass


def construct_linked_list(nums: List[int]) -> Optional[ListNode]:
    if len(nums) == 0:
        return None
    head = ListNode(nums[0])
    cur = head
    for num in nums[1:]:
        cur.next = ListNode(num)
        cur = cur.next
    return head


def get_nums(head: ListNode) -> List[int]:
    nums = []
    cur = head
    while cur:
        nums.append(cur.val)
        cur = cur.next
    return nums


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),
        ([1, 2, 3, 4, 5], 3, [1, 2, 3, 4, 5]),
    ]
    for case in cases:
        head = construct_linked_list(case[0])
        res_head = solution.reverseKGroup(head, case[1])
        res = get_nums(res_head)
        print(res, case[-1])
