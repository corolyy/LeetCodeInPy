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

        思路: 排序 + 双指针 + 剪枝
        实现:
           - 固定1个数, 另外2个数退化成2Sum = 0 - num1, 双指针夹逼即可
           - 排序之后方便剪枝(最小值 < 0 - num1则无解)
           - 遍历时去除重复采样
        """
        # 不满足条件
        if not nums or len(nums) < 3:
            return []
        # 排序, 方便 双指针 及 剪枝
        nums.sort()
        nums_len, result = len(nums), []
        for idx in range(0, nums_len):
            # 剪枝: 最小值 ＞ 0, 后续不需考量
            if nums[idx] > 0:
                break
            # 剪枝: 已考量过的2Sum, 不需重复考量
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            # 退化成2Sum
            target, l, r = - nums[idx], idx + 1, nums_len - 1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                    # 剪枝: 去除重复的左侧考察项
                    while l < nums_len and nums[l] == nums[l - 1]:
                        l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                    # 剪枝: 去除重复的右侧考察项
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                else:
                    result.append([nums[idx], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # 剪枝: 去除重复的左侧考察项
                    while l < nums_len and nums[l] == nums[l - 1]:
                        l += 1
                    # 剪枝: 去除重复的右侧考察项
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
        return result
