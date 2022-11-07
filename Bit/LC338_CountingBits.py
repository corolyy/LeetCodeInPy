# coding: utf-8
"""338. 比特位计数
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

示例 1:

输入: 2
输出: [0,1,1]
示例 2:

输入: 5
输出: [0,1,1,2,1,2]
进阶:

给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
要求算法的空间复杂度为O(n)。
你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。
"""
from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        '''位运算 + 缓存

        思路:
            - 对于2的N次幂, 有x & (x - 1) = 0的性质
            - 对于非2的N次幂, 其1的位数 =  x与最靠近x的2的幂取模后的值的1的位数 + 1
                如 7 % 4 = 3
                7 -> 0111
                3 -> 0011
        实现:
            - 缓存最近的2的幂
            - 缓存所有值的位数
        复杂度:
            time: O(N)
            space: O(N)
        '''
        latest_power, cnt_cache = 0, {0: 0}
        rst = [0]
        for i in range(1, num + 1):
            if i & i - 1 == 0:
                cnt_cache[i] = 1
                latest_power = i
                rst.append(1)
            else:
                cnt_cache[i] = cnt_cache[i % latest_power] + 1
                rst.append(cnt_cache[i])
        return rst

    def countBitsBruteForce(self, num: int) -> List[int]:
        '''位运算(暴力版)

        思路: 利用x & (x - 1)会移除最后1位1的性质, 对范围内的每个数字进行计数
        复杂度:
            time: O(N^M)
            space: O(N)
        '''
        rst = [0]
        for i in range(1, num + 1):
            cnt, tmp = 0, i
            while tmp:
                tmp &= tmp - 1
                cnt += 1
            rst.append(cnt)
        return rst
