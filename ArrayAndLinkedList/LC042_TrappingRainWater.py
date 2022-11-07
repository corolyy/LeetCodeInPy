# coding: utf-8
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """天赋解题

        - 思路: 一个位置能接多少雨水，等于min(l_max, r_max) - h[i]
        - 实现: 从左到右遍历获取每个位置的l_max列表, 从右到左遍历获取每个位置的r_max列表
        - 复杂度:
          time: O(N)
          space: O(N)
        """
        if not height:
            return 0

        l_max, r_max = [height[0]], height.copy()
        res = 0
        # 获取左侧最大列表
        for i, h in enumerate(height[1:], start=1):
            l_max.append(h if h > l_max[i - 1] else l_max[i - 1])
        # 获取右侧最大列表
        for i in range(len(height) - 2, -1, -1):
            r_max[i] = height[i] if height[i] > r_max[i + 1] else r_max[i + 1]

        # 计算答案
        for i in range(len(height)):
            res += min(l_max[i], r_max[i]) - height[i]
        return res
