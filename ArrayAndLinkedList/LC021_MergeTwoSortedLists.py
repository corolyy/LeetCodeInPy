# coding: utf-8
"""21. 合并两个有序链表
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例 1：
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]

示例 2：
输入：l1 = [], l2 = []
输出：[]

示例 3：
输入：l1 = [], l2 = [0]
输出：[0]

提示：
两个链表的节点数目范围是 [0, 50]
-100 <= Node.val <= 100
l1 和 l2 均按 非递减顺序 排列
"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''简单递归向下

        - 思路:
            - 终止条件: 两个node中一方为None即可
        '''
        def merge(node1,  node2):
            if node1 is None or node2 is None:
                return node1 or node2

            if node1.val < node2.val:
                node = node1
                node.next = merge(node1.next, node2)
            else:
                node = node2
                node.next = merge(node1, node2.next)
            return node

        return merge(l1, l2)
