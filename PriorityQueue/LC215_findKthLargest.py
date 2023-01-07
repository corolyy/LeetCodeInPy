"""215. 数组中的第K个最大元素
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。

示例 1:
输入: [3,2,1,5,6,4], k = 2
输出: 5

示例 2:
输入: [3,2,3,1,2,4,5,5,6], k = 4
输出: 4

提示：
1 <= k <= nums.length <= 105
-10^4 <= nums[i] <= 10^4
"""
import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """ 优先队列(大顶堆)

        思路: 构建大顶堆, pop K次即可得到结果
        """
        max_heap, nums_len = [], len(nums)
        # 构造大顶堆
        for num in nums:
            heapq.heappush(max_heap, num)
        # 连续pop(len - k - 1)次
        for idx in range(nums_len - k):
            heapq.heappop(max_heap)
        return heapq.heappop(max_heap)
