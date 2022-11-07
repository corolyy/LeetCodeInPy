# coding: UTF-8
"""977. 有序数组的平方
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。



示例 1：

输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100]
排序后，数组变为 [0,1,9,16,100]
示例 2：

输入：nums = [-7,-3,2,3,11]
输出：[4,9,9,49,121]


提示：

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums 已按 非递减顺序 排序


进阶：

请你设计时间复杂度为 O(n) 的算法解决本问题
"""
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        '''桶排序

        - 思路: 记录每位绝对值的个数，然后从0位开始累加
        - 复杂度:
            time: 因为桶排序和遍历桶都是O(N)，所以总的是O(N)
        '''
        if nums[0] >= 0:
            return [i * i for i in nums]
        if nums[-1] <= 0:
            return [i * i for i in nums[-1::-1]]
        bucket_size = max(-nums[0], nums[-1]) + 1
        bucket = [0] * bucket_size
        for num in nums:
            idx = -num if num < 0 else num
            bucket[idx] = bucket[idx] + 1
        res = []
        for idx, val in enumerate(bucket):
            while val > 0:
                res.append(idx * idx)
                val -= 1
        return res
