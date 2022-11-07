# coding: utf-8
"""2. 两数相加
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。



示例 1：


输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
示例 2：

输入：l1 = [0], l2 = [0]
输出：[0]
示例 3：

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]


提示：

每个链表中的节点数在范围 [1, 100] 内
0 <= Node.val <= 9
题目数据保证列表表示的数字不含前导零
"""


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ''' 递归

        - 思路: 从首节点向下递归，每层生成新节点，并且将下一层节点作为next值
        - 实现:
            1. 向下递归;
            2. 链表长度可能不相等，终止条件为or;
            3. 向下传递进位信息, 注意进位信息可能会造成超出原长度的最高位节点.
        - 复杂度:
            time: O(N)
            space: O(N)
        '''

        def add_node(l, r, cnt):
            if not l and not r and not cnt:
                return None

            num = cnt
            num += l.val if l else 0
            num += r.val if r else 0
            cur, nxt = num % 10, num // 10
            node = ListNode(cur, add_node(l.next if l else None,
                                          r.next if r else None,
                                          nxt))
            return node

        return add_node(l1, l2, 0)

    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ''' 利用列表

        - 思路: 顺序遍历链表，再顺序相加，遍历组链，注意进位
        - 复杂度:
          time: O(N)
          space: O(N)
        '''
        node_list, inc = [], 0
        # 入栈`
        while l1 or l2:
            tmp = inc
            if l1:
                tmp += l1.val
                l1 = l1.next
            if l2:
                tmp += l2.val
                l2 = l2.next
            node_list.append(ListNode(val=tmp % 10))
            inc = tmp // 10
        if inc:
            node_list.append(ListNode(val=inc))
        # 生成链表:
        for idx, node in enumerate(node_list[:-1]):
            node.next = node_list[idx + 1]
        return node_list[0]
