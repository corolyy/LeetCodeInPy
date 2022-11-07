# coding: utf-8
"""143. 重排链表
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1:
给定链表 1->2->3->4, 重新排列为 1->4->2->3.

示例 2:
给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        '''暴力法
        
        - 思路: 因为每个节点都会被操作，所以时间复杂度肯定不会小于O(N)
                直接拿数组缓存所有节点, 然后按下下标重新排序即可
        - 复杂度:
            time: O(N)
            space: O(N)
        '''
        if not head or not head.next:
            return head

        node_list = []
        pointer = head
        while pointer:
            node_list.append(pointer)
            pointer = pointer.next

        length = len(node_list)
        start, end = 0, length - 1
        pre_end = None
        while start < end:
            # 与前序对接
            if pre_end:
                node_list[pre_end].next = node_list[start]
            # 处理本组节点
            node_list[start].next = node_list[end]
            node_list[end].next = None
            # 处理坐标
            pre_end = end
            start += 1
            end -= 1
        # 处理节点数为奇数的场景
        if length % 2:
            mid = length // 2
            node_list[pre_end].next = node_list[mid]
            node_list[mid].next = None
