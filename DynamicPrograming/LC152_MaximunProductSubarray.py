# coding: utf-8
"""152. 乘积最大子数组
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。



示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''分治法

        思路:
            - 按0分段，最终比较各段最大值，有0则带上0一起
            - 段内无0，故乘积需要考虑负数的多少：
                - 无负数，则从头乘到尾
                - 有负数:
                    - 偶数个: 从头乘到尾
                    - 奇数个:
                        - 1个:
                            - 仅一个数字，直接返回
                            - 两端相乘，大者返回
                        - 大于3个:
                            从头乘到第一个负数l，从第一个负数之后乘到最后一个负数之前mid，从最后一个负数乘到倒数第一个数r
                            返回max(l * mid, mid * f)

        '''
        '''分治法

        思路:
            - 按0分段，最终比较各段最大值，有0则带上0一起
            - 段内无0，故乘积需要考虑负数的多少：
                - 无负数，则从头乘到尾
                - 有负数:
                    - 偶数个: 从头乘到尾
                    - 奇数个:
                        - 1个:
                            - 仅一个数字，直接返回
                            - 两端相乘，大者返回
                        - 大于3个:
                            从头乘到第一个负数l，从第一个负数之后乘到最后一个负数之前mid，从最后一个负数乘到倒数第一个数r
                            返回max(l * mid, mid * f)
        复杂度:
            time: O(N)
            space: O(N)
        '''
        seg, rst_set = [], set()
        for num in nums:
            if num == 0:
                if seg:
                    rst_set.add(self._calc_max(seg))
                seg = []
                rst_set.add(num)
            else:
                seg.append(num)
        if seg:
            rst_set.add(self._calc_max(seg))
        return max(rst_set)

    def _calc_max(self, num_seg):
        def multi(num_list):
            x = 1
            for num in num_list:
                x *= num
            # print("----> nums: {}, rst: {}".format(num_list, x))
            return x

        # print("num_seg: {}".format(num_seg))
        # 只有一个数字
        if len(num_seg) == 1:
            return num_seg[0]

        # 计算各负数的坐标
        neg_idx = []
        for i, num in enumerate(num_seg):
            if num < 0:
                neg_idx.append(i)
        # print("neg_idx: {}".format(neg_idx))
        neg_cnt = len(neg_idx)
        # 偶数个负数，直接相乘
        if neg_cnt % 2 == 0:
            return multi(num_seg)

        # 只有一个负数的场景
        if neg_cnt == 1:
            if neg_idx[0] == 0:
                # 首为负，直接后部相乘
                return multi(num_seg[1:])
            elif neg_idx[0] == len(num_seg) - 1:
                # 尾为负，直接前部相乘
                return multi(num_seg[:-1])
            else:
                return max(multi(num_seg[:neg_idx[0]]),
                           multi(num_seg[neg_idx[0] + 1:]))

        # >= 3个负数
        if neg_idx[0] == 0 or neg_idx[-1] == len(num_seg) - 1:
            # 首或尾为负数，分别舍弃首尾取最大
            # print(num_seg)
            return max(multi(num_seg[neg_idx[0] + 1:]),
                       multi(num_seg[:neg_idx[-1]]))

        l = multi(num_seg[:neg_idx[0] + 1])
        mid = multi(num_seg[neg_idx[0] + 1: neg_idx[-1]])
        r = multi(num_seg[neg_idx[-1]:])
        return max(l * mid, r * mid)
