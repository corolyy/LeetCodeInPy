# coding: utf-8
"""54. 螺旋矩阵
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

示例 2：
输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]

提示：
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """ DFS变式
        思路: 按照右下左上顺序进行深度优先遍历即可
        实现:
          1. 递归 + Hash剪枝
          2. 顺时针旋转 = 尽量保持与上次方向一致(pre_dir) + 按右下左上优先
        复杂度:
           time: O(N) space: O(N)
        """
        result = []
        x_len, y_len = len(matrix), len(matrix[0])
        x_order, y_order = [0, 1, 0, -1], [1, 0, -1, 0]
        visited = set()

        def _dfs(x, y, pre_cnt):
            if (x, y) in visited:
                # print("\t{} visited".format((x, y)))
                return
            if not (0 <= x < x_len) or not (0 <= y < y_len):
                # print("\t{} out of range".format((x, y)))
                return
            result.append(matrix[x][y])
            visited.add((x, y))
            # print("X: {}, Y: {}, Val: {}".format(x, y, matrix[x][y]))
            for cnt in range(4):
                cur_cnt = (pre_cnt + cnt) % 4
                _dfs(x + x_order[cur_cnt], y + y_order[cur_cnt], cur_cnt)

        _dfs(0, 0, 0)
        return result
