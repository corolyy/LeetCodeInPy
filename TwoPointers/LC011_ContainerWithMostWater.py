# coding: utf-8
"""11. 盛最多水的容器
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器。



示例 1：



输入：[1,8,6,2,5,4,8,3,7]
输出：49
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
示例 2：

输入：height = [1,1]
输出：1
示例 3：

输入：height = [4,3,2,1,4]
输出：16
示例 4：

输入：height = [1,2,1]
输出：2


提示：

n = height.length
2 <= n <= 3 * 104
0 <= height[i] <= 3 * 104
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''双指针

        - 思路:
            对于高度为i, j的两根柱子，计算其容量后，应该让高度更小的柱子向内移动来寻找更大容量的可能
        - 复杂度:
            time: O(N)
            space: O(1)
        '''
        l, r = 0, len(height) - 1
        res = -float('inf')
        while l < r:
            res = max(res, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res

    def maxArea_brute_force(self, height: List[int]) -> int:
        '''暴力解法

        - 思路:
            计算每个位置为起点的最大容量
        - 复杂度:
            time: O(N**2)
            space: O(N)
        '''
        cap_list = [-float('inf')] * (len(height) - 1)
        for i, start in enumerate(height[:-1]):
            for j, end in enumerate(height[i + 1:], start=i + 1):
                cap_list[i] = max(cap_list[i], (j - i) * min(start, end))
        return max(cap_list)
