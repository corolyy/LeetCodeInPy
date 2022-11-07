# coding: utf-8
"""231. 2的幂
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

示例 1:
输入: 1
输出: true
解释: 2^0 = 1

示例 2:
输入: 16
输出: true
解释: 2^4 = 16

示例 3:
输入: 218
输出: false
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        '''位运算

        思路: 2^n其2进制只有一个1
            1 -> 0001
            2 -> 0010
            8 -> 1000
            同时x & (x - 1)将会移除最后一位1
            所以若x & (x - 1) == 0，则说明其为2的整数幂
        实现:
            - 例外: 0 & (0 - 1) == 0, 但0不是2的整数幂
            - 性能: 用例0只会出现1次，所以判断条件中 n != 0放在and后面，可以提升性能
        复杂度:
            time: O(1)
            space: O(1)
        '''
        return n & n - 1 == 0 and n != 0


s = Solution()
print(s.isPowerOfTwo(10))
print(s.isPowerOfTwo(0))
print(s.isPowerOfTwo(1))
print(s.isPowerOfTwo(4))
print(s.isPowerOfTwo(19))
print(s.isPowerOfTwo(-1))
