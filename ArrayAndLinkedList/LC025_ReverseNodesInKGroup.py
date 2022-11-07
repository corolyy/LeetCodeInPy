# coding: utf-8
""" 25. K 个一组翻转链表
给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。

k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

 

示例 1：
输入：head = [1,2,3,4,5], k = 2
输出：[2,1,4,3,5]

示例 2：
输入：head = [1,2,3,4,5], k = 3
输出：[3,2,1,4,5]

提示：
链表中的节点数目为 n
1 <= k <= n <= 5000
0 <= Node.val <= 1000
 

进阶：你可以设计一个只用 O(1) 额外内存空间的算法解决此问题吗？
"""
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def _reverse(self, head, stop_point):
        prev, cur = None, head
        while cur != stop_point:
            temp = cur.next
            cur.next = prev
            prev, cur = cur, temp
        return cur

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ''' 分治

        思路: k个一组分段翻转
        关键: 1. 记录好prev和tail
        复杂度:
            - space: O(K)
            - time: O(N)
        '''
        # 无需翻转
        if k < 2:
            return head

        start_head, prev_tail, cur_head, cur_tail, next_head = head, None, head, head, head.next
        while cur_head:
            for _ in range(1, k):
                # 凑不够K个, 该组无需翻转
                if not cur_tail:
                    return start_head
                cur_tail = cur_tail.next
            next_head = cur_tail.next
            # 翻转本组K个链表
            temp_head = self._reverse(cur_head, next_head)
            # 与前组对接
            if prev_tail:
                prev_tail.next = temp_head
            else:
                # 没有前一组这里就是本组的头
                start_head = temp_head
            # 与后一组对接
            cur_head.next = next_head
            cur_head = next_head
        return start_head
