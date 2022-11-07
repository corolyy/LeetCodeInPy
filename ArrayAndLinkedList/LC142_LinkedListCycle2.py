# coding: utf-8
"""142. 环形链表 II

给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。
说明：不允许修改给定的链表。

进阶：
你是否可以使用 O(1) 空间解决此题？

示例 1：
输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。

示例 2：
输入：head = [1,2], pos = 0
输出：返回索引为 0 的链表节点
解释：链表中有一个环，其尾部连接到第一个节点。

示例 3：
输入：head = [1], pos = -1
输出：返回 null
解释：链表中没有环。

提示：
链表中节点的数目范围在范围 [0, 104] 内
-105 <= Node.val <= 105
pos 的值为 -1 或者链表中的一个有效索引
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def _calc_cycle_length(self, head: ListNode) -> int:
        """ 判断是否有环，返回环的长度

        1. 是否有环：经典快慢指针
        2. 环的长度：感知有环后慢指针走一圈计数

        :param head: 头节点
        :return: -1 - 无环， N - 环的长度
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                temp = slow
                len = 1  # 即使是自指节点，也要走一步，所以从1开始计数
                while slow.next != temp:
                    len += 1
                    slow = slow.next
                return len
        return -1

    def _get_node(self, node: ListNode, distance: int) -> ListNode:
        """计算走了N步之后得到的节点"""
        for _ in range(distance):
            node = node.next
        return node

    def detectCycle(self, head: ListNode) -> ListNode:
        # 数学分析法
        # 思路:
        #    1. 先用快慢指针判断是否有环;
        #    2. 有环后马上开始走一圈，计算环的长度；(注意不能简单的用快步*2 - 慢步，会得到环长度的整数倍)；
        #    3. 从头开始走环的长度步数，直到一次走到当前节点，该节点坐标为所求
        # 复杂度:
        #   time O(2*N + N^2) space O(1)
        cycle_length = self._calc_cycle_length(head)
        if cycle_length < 0:
            return None

        while True:
            node = self._get_node(head, cycle_length)
            if node == head:
                return head
            head = head.next
