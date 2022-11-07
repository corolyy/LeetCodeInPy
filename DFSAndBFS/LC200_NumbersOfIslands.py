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

        - 思路: 遍历每个坐标, 遇到陆地时用DFS把该片陆地上的所有坐标都获取, 避免重复技术
        - 实现:
            - 岛屿数is_cnt
            - 已访问陆地Hash
        - 复杂度:
            time: O(M * N)
            space: O(M * N)
        '''
        def _dfs(row, col):
            # 深度优先, 将陆地标记为已访问
            for idx in range(4):
                x, y = row + r[idx], col + c[idx]
                if (x, y) in visited:
                    continue

                if not (0 <= x < m and 0 <= y < n):
                    # 防止越界
                    continue

                if grid[x][y] == '0':
                    continue

                visited.add((x, y))
                _dfs(x, y)

        visited, is_cnt = set(), 0
        m, n = len(grid), len(grid[0])
        r, c = [0, 0, 1, -1], [1, -1, 0, 0]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in visited:
                    is_cnt += 1
                    _dfs(i, j)
        return is_cnt
