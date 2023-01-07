# coding: utf-8
"""3. 无重复字符的最长子串

示例 1:
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

提示：
0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ''' 滑动窗口

        思路: 子串什么的, 想想滑动窗口
        实现关键:
          1. 滑动条件:
            - 没重复时右指针扩张, 重复时左指针收缩
            - 重复时记录长度: l - r + 1
            - 左指针收缩, 直至遇到第一个非重复
          2. 注意边界
            - r < len
          3. 使用set记录重复
        '''
        l, r, visited, max_len = 0, 0, set(), 0
        while r < len(s):
            # 直接判断是否需要收缩
            while s[r] in visited:
                visited.remove(s[l])
                l += 1
            visited.add(s[r])
            max_len = max(max_len, r - l + 1)
            # 开始扩张
            r += 1
        return max_len

