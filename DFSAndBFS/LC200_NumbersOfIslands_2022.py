# coding: utf-8
"""200. 岛屿数量
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。



示例 1：

输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1
示例 2：

输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3


提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] 的值为 '0' 或 '1'
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''DFS法

        - 思路: 遍历每个坐标, 遇到陆地时用DFS把相邻的陆地都淹掉(包括自己, 1 -> 0)
        - 实现:
            - 岛屿数is_cnt
            - 注水而不是维护visited表，降低空间复杂度
        - 复杂度:
            time: O(M * N)
            space: O(1)
        '''
        def _dfs_flood(x, y):
            # 先淹自己
            grid[x][y] = "0"
            # 上下左右
            for step in range(4):
                col_idx, row_idx = x + col[step], y + row[step]
                # 处理越界
                if not (0 <= col_idx < x_len and 0 <= row_idx < y_len):
                    continue
                # 忽略水域
                if grid[col_idx][row_idx] != "1":
                    continue
                _dfs_flood(col_idx, row_idx)

        cnt, x_len, y_len = 0, len(grid), len(grid[0])
        # 行(x, column), 列(y, row)遍历矩阵
        col = [1, -1, 0, 0]
        row = [0, 0, 1, -1]
        for x in range(x_len):
            for y in range(y_len):
                if grid[x][y] == "1":
                    cnt += 1
                    _dfs_flood(x, y)
        return cnt
