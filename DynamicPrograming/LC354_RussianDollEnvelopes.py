# coding: utf-8
"""354. 俄罗斯套娃信封问题
给你一个二维整数数组 envelopes ，其中 envelopes[i] = [wi, hi] ，表示第 i 个信封的宽度和高度。

当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。

请计算 最多能有多少个 信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。

注意：不允许旋转信封。


示例 1：

输入：envelopes = [[5,4],[6,4],[6,7],[2,3]]
输出：3
解释：最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。
示例 2：

输入：envelopes = [[1,1],[1,1],[1,1]]
输出：1


提示：

1 <= envelopes.length <= 5000
envelopes[i].length == 2
1 <= wi, hi <= 104
"""
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        '''动态规划

        - 思路: 先按元素x[0], x[1]从小到大排序
            - 状态定义: dp[i], 第i大的能套几个
            - 转移方程: dp[i] = max(dp[j]), e[j][0] < e[i][0], e[j][1] < e[i][i]
            - 解: max(dp)
            - base case: dp[i] = 1
        '''
        dp = [1] * len(envelopes)
        envelopes.sort(key=lambda x: (x[0], x[1]))

        for idx in range(1, len(envelopes)):
            tmp = []
            for j in range(idx):
                if envelopes[j][0] < envelopes[idx][0] and envelopes[j][1] < envelopes[idx][1]:
                    tmp.append(dp[j])
            if tmp:
                dp[idx] += max(tmp)
        return dp[-1]


s = Solution()
print(s.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
print(s.maxEnvelopes([[1,1],[1,1],[1,1]]))