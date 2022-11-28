""" 快排

思想: 分治
实现: 递归
关键: partition函数

def partition(nums, l, r):
    # 原理: 选择nums[l:r + 1]中的一个数字作为中轴pivot，使得pivot左侧都比它小，右侧都比它大
    # 实现: 双指针, 从两端向中心夹逼，右侧遇到小于pivot停止，左侧遇到大于pivot停止，交换之后开启下一轮
    # 返回: pivot坐标


def quick_sort(nums, l, r):
    # 原理: 向下递归，利用partition函数使递归树每层有序度递增，递归到底层时全部有序
    # 复杂度:
    #   space: O(1), 原地排序
    #   time: O(N * lgN)
    #   稳定性: pivot移动时忽略eq场景，应该可以保持稳定(存疑)
    if l >= r:
        return

    pivot_idx = partition(nums, 0, len(nums) - 1)
    partition(nums, 0, pivot)
"""
from random import Random

random_inst = Random()


def swap(num_list, idx_0, idx_1):
    num_list[idx_0], num_list[idx_1] = num_list[idx_1], num_list[idx_0]


def partition(num_list, l, r):
    # 随机选择, 打破最坏条件
    pivot_idx = random_inst.randint(l, r)
    # 不交换到头指针的话，后面找pivot_idx会比较复杂
    swap(num_list, l, pivot_idx)
    pivot_val = num_list[l]
    while l < r:
        # 右指针找到小于pivot的第一个数
        while l < r and num_list[r] >= pivot_val:
            r = r - 1
        # 交换小于pivot的第一个数和pivot，这样pivot左侧有序度不变，右侧递增
        swap(num_list, l, r)
        # 左指针找到大于pivot的第一个数
        while l < r and num_list[l] <= pivot_val:
            l = l + 1
        # 交换大于pivot的第一个数和pivot，这样pivot右侧有序度不变，左侧递减
        swap(num_list, l, r)
        # 一轮循环结束，保证pivot还在l，l左侧 <= pivot, r右侧 >= pivot即可
    return l


def quick_sort(num_list, l, r):
    # 递归终止条件
    if l >= r:
        return

    # 有点像前序遍历
    pivot_idx = partition(num_list, l, r)
    quick_sort(num_list, l, pivot_idx - 1)
    quick_sort(num_list, pivot_idx + 1, r)


if __name__ == "__main__":
    num_list = [9, 1, 8, 9, 2, 7, 4, 3, 6, 4, 5]
    quick_sort(num_list, 0, len(num_list) - 1)
    print(num_list)
