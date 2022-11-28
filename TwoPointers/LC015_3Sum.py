"""15. 三数之和
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请
你返回所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。

示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。

示例 2：
输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。

示例 3：
输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。

提示：
3 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """ 双指针 + 排序

        思路: 双指针 + 排序 + 剪枝
        实现:
           - 固定1个数, 另外2个数退化成2Sum = 0 - num1, 双指针夹逼即可
           - 排序之后方便剪枝(最小值 < 0 - num1则无解)
           - 使用set去重，由于前序目标搜索空间涵盖后序目标, 所以后序目标与前序目标重复时可以直接跳过
        """
        res, searched_set, length = [], set(), len(nums)
        nums = sorted(nums)
        for idx, num in enumerate(nums):
            # 边界保护: idx至多为 length - 3
            if idx > length - 3:
                break
            # 初始化目标与左右指针
            target, low, high = -num, idx + 1, length - 1
            # 剪枝: 去重
            if target in searched_set:
                continue
            searched_set.add(target)

            while low < high:
                # 剪枝: 去不可能
                if nums[low] > target:
                    break
                low_val, high_val = nums[low], nums[high]
                total = low_val + high_val
                if total > target:
                    while low < high and nums[high] == high_val:
                        # 剪枝: 过滤相同high值
                        high -= 1
                elif total < target:
                    while low < high and nums[low] == low_val:
                        # 剪枝: 过滤相同low值
                        low += 1
                else:
                    res.append([num, nums[low], nums[high]])
                    while low < high and nums[low] == low_val:
                        # 剪枝: 过滤相同low值
                        low += 1
                    while low < high and nums[high] == high_val:
                        # 剪枝: 过滤相同high值
                        high -= 1

        return res
