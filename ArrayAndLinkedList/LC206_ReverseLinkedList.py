# coding: utf-8

"""206. 反转链表

反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverse_list_briefly(self, head: ListNode) -> ListNode:
        # 递推法
        # 原理: 反转指针之后需要保留下一个对象，这样就能迭代下去，直到当前实例为None
        # 复杂度: time O(N) space O(1)
        pre, cur = None, head
        while cur is not None:
            pre, cur.next, cur = cur, pre, cur.next
        return pre
    def reverse_list(self, head: ListNode) -> ListNode:
        # 递推法
        # 原理: 反转指针之后需要保留下一个对象，这样就能迭代下去，直到当前实例为None
        # 复杂度: time O(N) space O(1)
        pre, cur = None, head
        while cur is not None:
            temp = cur.next
            cur.next = pre
            pre, cur = cur, temp
        return pre

    def reverse_list_brute_force(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        # 暴力法
        # 原理: 遍历每个节点，倒叙连接即可
        # 复杂度: time O(N) space O(N)
        container_list = []
        while head:
            container_list.append(head)
            head = head.next

        container_list[0].next = None
        for i, node in enumerate(container_list, 1):
            node.next = container_list[i - 1]
        return container_list[-1]
