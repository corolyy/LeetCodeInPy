# coding: utf-8
"""93. 复原 IP 地址

给定一个只包含数字的字符串，用以表示一个 IP 地址，返回所有可能从 s 获得的 有效 IP 地址 。你可以按任何顺序返回答案。
有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。

示例 1：
输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]

示例 2：
输入：s = "0000"
输出：["0.0.0.0"]

示例 3：
输入：s = "1111"
输出：["1.1.1.1"]

示例 4：
输入：s = "010010"
输出：["0.10.0.10","0.100.1.0"]

示例 5：
输入：s = "101023"
输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

提示：
0 <= s.length <= 3000
s 仅由数字组成
"""
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        '''回溯

        - 思路: 以每一位为起点向下回溯, 回溯时明确当前是IP的第几段, 在第四段找到合法值时即为终止条件
        '''
        def back_track(start_idx, pre_seg):
            if len(pre_seg) == 4:
                res_list.append(".".join(pre_seg))
                return

            if start_idx >= length:
                return

            if start_idx + 2 < length:
                seg = s[start_idx: start_idx + 3]
                if s[start_idx] != '0' and int(seg) <= 255:
                    pre_seg.append(seg)
                    back_track(start_idx + 3, pre_seg)
                    pre_seg.pop()

            if start_idx + 1 < length:
                if s[start_idx] != '0':
                    pre_seg.append(s[start_idx: start_idx + 2])
                    back_track(start_idx + 2, pre_seg)
                    pre_seg.pop()

            pre_seg.append(s[start_idx])
            back_track(start_idx + 1, pre_seg)
            pre_seg.pop()

        res_list, length = [], len(s)
        for idx in range(len(s)):
            back_track(idx, [])
        return res_list
