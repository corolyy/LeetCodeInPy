'''Longest Palindromic Substring
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        ''' 动态规划

        思路: 不仅找最值，还要记录路径，尝试使用动态规划
        DP分析:
          - 状态定义:
            dp[i][j] = True/False, 坐标i为(左)中心, 长度为j的回文串是否存在
          - 选择&转移:
            - 长度为奇数, j % 2 != 0
              1. 前置回文, dp[i][j - 2] == True, j - 2 >= 0
              2. 不能越界, 半径radius = j // 2
                 i - radius >= 0, i + radius <= len
              3. 两端相等
                 s[i - radius] == s[i + radius]
            - 长度为偶数, j % 2 == 0
              1. 前置回文, dp[i][j - 2] == True, j - 2 >= 0
              2. 不能越界, 半径radius = j // 2
                i + 1 - radius >= 0, i + radius < len
              3. 两端相等
                s[i + 1 - radius] ==  s[i + radius]
          - base case:
            dp[.][0], dp[.][1] = True, True
          - 解:
            倒序遍历结果找到最大直接进入下一轮: max(dp[i][j]) => i, j => 字符串截取
        实现关键:
          1. 扩展越界时直接停止扩展
          2. 倒序
        复杂度:

        '''
        s_len = len(s)
        src, max_len = 0, 1
        dp = [[True if j < 2 else False for j in range(s_len + 1)] for _ in range(s_len)]
        for i in range(s_len):
            # 直接从长度2开始
            for j in range(2, s_len + 1):
                # 判断是否有更短子串
                if not(dp[i][j - 2]):
                    continue
                radius = j // 2
                if j % 2 == 0:
                    # 偶数长度
                    if not ((i + 1 - radius >= 0) and (i + radius) < s_len):
                        # 扩展越界
                        break
                    if s[i + 1 - radius] == s[i + radius]:
                        dp[i][j] = True
                        if j > max_len:
                            src, max_len = i + 1 - radius, j
                            # print(src, max_len)
                else:
                    # 奇数长度
                    if not ((i - radius  >= 0) and (i + radius < s_len)):
                        # 扩展越界
                        break
                    if s[i - radius] == s[i + radius]:
                        dp[i][j] = True
                        if j > max_len:
                            src, max_len = i - radius, j
                            # print(src, max_len)
        # print(dp)
        # 截取字符串
        return s[src : src + max_len]
