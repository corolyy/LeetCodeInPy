# coding: utf-8
"""24. 两两交换链表中的节点
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1：
输入：head = [1,2,3,4]
输出：[2,1,4,3]

示例 2：
输入：head = []
输出：[]

示例 3：
输入：head = [1]
输出：[1]

提示：
链表中节点的数目在范围 [0, 100] 内
0 <= Node.val <= 100
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 递推法
        # 思路: 与反转列表类似，2个一组内部反转即可，记录第3节点作为下一次的head，记录新的2节点在下一次完成后重新链接
        # 复杂度: time O(N) space O(1)
        if head is None or head.next is None:
            return head

        cur_0, cur_1, pre = head, head.next, None
        head = cur_1
        while cur_0 and cur_1:
            temp = cur_1.next
            cur_0.next, cur_1.next = None, cur_0
            if pre:
                pre.next = cur_1

            if temp and temp.next:
                pre = cur_0
                cur_0, cur_1 = temp, temp.next
            else:
                # 最后一次没必要循环了
                cur_0.next = temp
                break

        return head
