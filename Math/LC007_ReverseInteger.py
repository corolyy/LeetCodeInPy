# coding: utf-8
"""7. 整数反转
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）。


示例 1：

输入：x = 123
输出：321
示例 2：

输入：x = -123
输出：-321
示例 3：

输入：x = 120
输出：21
示例 4：

输入：x = 0
输出：0


提示：

-231 <= x <= 231 - 1
"""


class Solution:
    def reverse(self, x: int) -> int:
        '''暴力法

        - 思路: 对10整除/取模 -> 逆序乘10/累加
        '''
        res, flag = 0, -1 if x < 0 else 1
        x = x * flag
        while x != 0:
            res *= 10
            res += x % 10
            x //= 10
        res *= flag
        return res if -2147483648 < res < 2147483647 else 0
