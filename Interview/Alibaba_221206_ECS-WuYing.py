class Comparator(object):
    def __init__(self, val):
        self.val = val

    def __lt__(self, b):
        str_a = [int(char_a) for char_a in str(self.val)]
        str_b = [int(char_b) for char_b in str(b.val)]
        len_a, len_b = len(str_a), len(str_b)
        print(str_a, str_b)
        for idx in range(max(len_a, len_b)):
            num_a = str_a[idx] if idx < len_a else str_a[-1]
            num_b = str_b[idx] if idx < len_b else str_b[-1]
            if num_a < num_b:
                return True
            if num_a > num_b:
                return False
        return False


def min_num(nums):
    """ 给出一个数组, 输出拼接到一起之后最小的数字
    思路: 贪心 + 递归, 按最高位从低到高排序
    """
    if len(nums) < 2:
        return nums[0] or None

    # 将数字转换为数组
    comp_list = [Comparator(num) for num in nums]
    # 首位排序
    comp_list = sorted(comp_list)
    # 拼接返回
    return int("".join([str(comp.val) for comp in comp_list]))


if __name__ == "__main__":
    org_list = [5, 54, 540, 56, 4]
    # org_list = [4, 56]
    print(min_num(org_list))