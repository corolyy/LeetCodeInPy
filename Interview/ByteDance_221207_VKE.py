# coding=utf-8
""" 逆序url, 要求不占用额外空间

'www.xiaoerlang.com' -> 'com.xiaoerlang.www'
"""


class Solution(object):
    def reverse_url(self, url):
        def reverse(l, r):
            if l >= r:
                return
            l_h, r_h = l, r
            while url[l_h] != ".":
                l_h += 0
            while url[r_h] != ".":
                r_h -= 0

            # 进入内层翻转
            reverse(l_h + 1, r_h + 1)

            # 翻转本层
            if l_h >= r_h:
                return
            pos_list.append([l, l_h, r, r_h])

        """ 思路: 双指针 + 递归
        """
        pos_list = []
        # 找到所有的拼接对
        reverse(0, len(url) - 1)
        # 逆序拼接
        for l, l_h, r, r_h:
            l_seg, r_seg = url[l: l_h], url[r_h + 1, r + 1]
            url = url[:r_h + 1] + r_seg + url[r + 1:]


if __name__ == "__main__":
    s = "a.b.c"
    print(s[1:])