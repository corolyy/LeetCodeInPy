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
        """ 快排拓展

        思路: partition分治
        """
        def swap(idx_0, idx_1):
            nums[idx_0], nums[idx_1] = nums[idx_1], nums[idx_0]

        def partition(left, right):
            # 随机取pivot
            pivot_idx = self._random_inst.randint(left, right)
            # pivot置于首位, 固定partition坐标
            swap(left, pivot_idx)
            pivot = nums[left]
            while left < right:
                # 右指针找到比pivot小的第一个数，与pivot互换，保证right往右都不比pivot小
                while left < right and nums[right] >= pivot:
                    right -= 1
                swap(left, right)
                # 左指针找到pivot大的第一个数，与pivot互换，保证left向左都不比pivot大
                while left < right and nums[left] <= pivot:
                    left += 1
                swap(left, right)  # 此时pivot又回到了left位
                # 继续下一轮，每一轮有序度都在增加
            return left

        # 确认目标顺位
        target = len(nums) - k

        # 迭代寻找目标
        l, r = 0, len(nums) - 1
        while l < r:
            piv_idx = partition(l, r)
            if target == piv_idx:
                return nums[piv_idx]

            if target < piv_idx:
                # target比pivot小, 在左区间
                r = piv_idx - 1
            else:
                # target比pivot大，在右区间
                l = piv_idx + 1

        return nums[target]
