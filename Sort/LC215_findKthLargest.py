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
from typing import List
from random import Random


class Solution:
    def __init__(self):
        self._random_inst = Random()

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """ 快排, partition得到pivot坐标为len - k即可

        实现: 根据pivot坐标与(len -k)相对大小判断向左/向右偏序分治即可, 不需要全量排序
        """
        def partition(left, right):
            pivot, l, r = nums[left], left, right
            while l < r:
                while l < r and nums[r] >= pivot:
                    r -= 1
                nums[l] = nums[r]
                while l < r and nums[l] <= pivot:
                    l += 1
                nums[r] = nums[l]
            nums[l] = pivot
            return l

        target, l_idx, r_idx = len(nums) - k, 0, len(nums) - 1
        while l_idx < r_idx:
            pivot_idx = partition(l_idx, r_idx)
            if pivot_idx > target:
                r_idx = pivot_idx - 1
            elif pivot_idx < target:
                l_idx = pivot_idx + 1
            else:
                return nums[target]
        return nums[target]
