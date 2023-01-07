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
def partition(num_list, left, right):
    """
    思路:
        1. 多轮调整，每轮只调整一组数据(有序度提高0~2)
        2. 选择最左侧元素作为pivot, 交换过程:
           a) 每1轮从右向左找到第1个比pivot小的, 放到当前左侧;
           b) 每1轮从左向右找到第1个比pivot大的, 放到当前右侧;
           c) 最终当前左坐标与右坐标相等，将pivot置于此处;
    优化:
        1. 随机选择元素作为pivot, 和最左侧交换
    """
    pivot, l, r = num_list[left], left, right
    while l < r:
        while l < r and num_list[r] >= pivot:
            r -= 1
        num_list[l] = num_list[r]
        while l < r and num_list[l] <= pivot:
            l += 1
        num_list[r] = num_list[l]
    num_list[l] = pivot
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
