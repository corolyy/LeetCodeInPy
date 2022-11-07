# coding: utf-8
"""242. 有效的字母异位词
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t:
            return True

        if s is None or t is None or len(s) != len(t):
            return False

        '''Hash法:
        
        原理: 统计s、t中每个字母出现次数，全部相同则满足要求
        '''

        calc_map = {}
        for index, s_str in enumerate(s):
            calc_map[s_str] = calc_map.get(s_str, 0) + 1
            t_str = t[index]
            calc_map[t_str] = calc_map.get(t_str, 0) - 1
        for val in calc_map.values():
            if val != 0:
                return False
        return True
