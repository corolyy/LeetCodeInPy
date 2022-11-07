# coding: utf-8
"""120. 三角形最小路径和
给定一个三角形 triangle ，找出自顶向下的最小路径和。

每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。



示例 1：

输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
输出：11
解释：如下面简图所示：
   2
  3 4
 6 5 7
4 1 8 3
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
示例 2：

输入：triangle = [[-10]]
输出：-10


提示：

1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104


进阶：

你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题吗？
"""
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        '''动态规划

        思路:
            - 从顶向下依次计算到当前节点的最小代价
            - 最小代价: f(i, j) = num[i, j] + min(num[i - 1, j], num[i - 1, j - 1])
        实现:
            注意边界
        复杂度:
            time: O(N)
            space: O(1)
        '''
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                pre_len = len(triangle[i - 1])
                if 0 < j < pre_len:  # 本行中间坐标
                    triangle[i][j] = triangle[i][j] + min(triangle[i - 1][j], triangle[i - 1][j - 1])
                elif j == pre_len:  # 本行尾坐标
                    triangle[i][j] = triangle[i][j] + triangle[i - 1][j - 1]
                else:  # 本行首坐标
                    triangle[i][j] = triangle[i][j] + triangle[i - 1][j]
        return min(triangle[-1])
