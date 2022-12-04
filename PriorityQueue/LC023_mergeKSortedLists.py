"""23. 合并K个升序链表
给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。

示例 1：
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6

示例 2：
输入：lists = []
输出：[]

示例 3：
输入：lists = [[]]
输出：[]

提示：
k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] 按 升序 排列
lists[i].length 的总和不超过 10^4
"""
import heapq
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """ 多指针 + 优先队列

        思路: 多指针构建小顶堆, 每次从堆顶取元素作为next
        """
        def lt(self, other):
            return self.val < other.val
        # 设置比较器
        ListNode.__lt__ = lt
        # 设置dummy_node
        dummy_node, heap = ListNode(-1), []
        pre_node = dummy_node
        for node in lists:
            if node:
                heapq.heappush(heap, node)
        while heap:
            node = heapq.heappop(heap)
            pre_node.next = node
            pre_node = node
            if node.next:
                heapq.heappush(heap, node.next)
        return dummy_node.next
