from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # 维护两个列表 small 和 large
        small, large = None, None
        cur_small, cur_large = None, None
        cur = head
        while cur:
            print(cur.val, cur.next)
            next_node = cur.next
            if cur.val < x:
                if small is None:
                    small = cur
                    cur_small = cur
                else:
                    cur_small.next = cur
                    cur_small = cur_small.next
            else:
                if large is None:
                    large = cur
                    cur_large = large
                else:
                    cur_large.next = cur
                    cur_large = cur_large.next
            # 需要端开下一个节点的连接
            cur.next=None
            cur = next_node

        if cur_small is None:
            return large

        cur_small.next = large
        return small

    def partition2(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # 转化成列表处理
        array = get_array_from_linked_list(head)
        less_x = []
        larger_x = []
        for num in array:
            if num < x:
                less_x.append(num)
            else:
                larger_x.append(num)
        new_array = less_x + larger_x
        return construct_linked_list(new_array)


def construct_linked_list(array) -> Optional[ListNode]:
    if not array: return None
    head = ListNode(array[0])
    cur = head
    for value in array[1:]:
        cur.next = ListNode(value)
        cur = cur.next
    return head


def get_array_from_linked_list(head: ListNode) -> List[int]:
    res = []
    cur = head
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([1, 4, 3, 2, 5, 2], 3, [1, 2, 2, 4, 3, 5]),
        ([2, 1], 2, [1, 2])
    ]
    for case in cases:
        linked_list = construct_linked_list(case[0])
        res_link_list = solution.partition(linked_list, case[1])
        res_array = get_array_from_linked_list(res_link_list)
        print(res_array, case[-1])
