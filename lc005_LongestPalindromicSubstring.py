'''Longest Palindromic Substring
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''


class Solution:
    def __init__(self):
        self.max_sub_len = 0
        self.max_sub_str = ""

    def longestPalindrome(self, s: str) -> str:
        '''逻辑法...

        思路: 回文子串, a -> cac -> bcacb or aa -> caac -> bcaacb
        实现: 对于每一位，都考量以其为中心的奇数子串和偶数子串
        '''
        def palindrome(l_idx, r_idx):
            '''该子串左侧和右侧的扩展起点'''
            if r_idx >= length or s[l_idx] != s[r_idx]:
                return

            l, r = l_idx, r_idx
            while l >= 0 and r < length and s[l] == s[r]:
                l -= 1
                r += 1
            sub_len = r - l - 1

            if sub_len > self.max_sub_len:
                self.max_sub_len = sub_len
                self.max_sub_str = s[l + 1: r]

        length = len(s)
        for i in range(length):
            palindrome(i, i)
            palindrome(i, i + 1)
        return self.max_sub_str

    def longestPalindrome_2020(self, s: str) -> str:
        if len(s) <= 1:
            return s

        max_len, max_index = 1, 0
        str_len = len(s)
        for i in range(str_len - 1):
            if 2 * min(i + 1, str_len - i - 1) < max_len:
                break
            
            if s[i] == s[i + 1]:
                half = 1
                for j in range(1, min(i + 1, str_len - i - 1)):
                    if s[i - j] != s[i + 1 + j]:
                        break
                    half += 1
                length = half * 2
                if length > max_len:
                    max_index = i
                    max_len = length

            if i > 0 and s[i - 1] == s[i + 1]:
                half = 0
                for j in range(min(i, str_len - i - 1)):
                    if s[i - 1 - j] != s[i + 1 + j]:
                        break
                    half += 1
                length = half * 2 + 1
                if length > max_len:
                    max_index = i
                    max_len = length

        if max_len % 2 != 0:
            half = int((max_len - 1) / 2)
            start, end = max_index - half, max_index + half + 1
        else:
            half = int(max_len / 2)
            start, end = max_index - half + 1, max_index + half + 1
        return s[start: end]


print(Solution().longestPalindrome("abb"))
print(Solution().longestPalindrome("bbb"))
print(Solution().longestPalindrome("cbbd"))