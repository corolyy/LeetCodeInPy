# coding: utf-8
"""3. 无重复字符的最长子串
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。



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
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
示例 4:

输入: s = ""
输出: 0


提示：

0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''Hash + 双指针

        - 思路:
            1. header + tail双指针扫描链表, 将元素添加到set()中;
            2. 每次找到重复元素时, 需要将头指针指向重复元素的下一个元素, 同时记录长度;
        - 实现:
            1. 使用hash表记录每个字符串最后一次出现的位置;
            2. 最后一段不重复的字符串在主循环中不被统计，需要单独计数;
            3. 注意头指针不是每次出现重复字符时都需要更新
        - 复杂度:
            time: O(N)
            space: O(N)
        '''
        if not s:
            return 0

        char_idx_map, max_dist = {s[0]: 0}, 1
        head = 0
        for idx, char in enumerate(s[1:], start=1):
            if char in char_idx_map:
                dist = idx - head
                max_dist = max(dist, max_dist)
                head = max(char_idx_map[char] + 1, head)
            char_idx_map[char] = idx
        # 处理最后一段
        if head != len(s) - 1:
            max_dist = max(max_dist, len(s) - head)
        return max_dist
