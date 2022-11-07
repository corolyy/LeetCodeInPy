'''
32. Longest Valid Parentheses
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) < 2:
            return 0
        stack, length = [], len(s)
        for i in range(length):
            if stack:
                if s[i] == ")" and s[stack[-1]] == "(":
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        if not stack:
            return length
        index, max_len = length, stack[0]
        while stack:
            last = stack.pop()
            tmp = index - last - 1
            max_len = max_len if max_len > tmp else tmp
            index = last
        return max_len


    def longestValidParentheses_no_stack(self, s: str) -> int:
        if len(s) < 2:
            return 0
        range_list = []
        start = 0
        length = len(s)
        while start < length - 1:
            if not (s[start] == self.l and s[start + 1] == self.r):
                start += 1
                continue
            s_index, e_index = start, start + 1
            while s_index - 1 >= 0 and e_index + 1 < length:
                if s[s_index - 1] == self.l and s[e_index - 1] == self.r:
                    s_index -= 1
                    e_index += 1
                else:
                    break
            if range_list and range_list[-1][1] == s_index - 1:
                range_list[-1][1] = e_index
            else:
                range_list.append([s_index, e_index])
            start = e_index + 1
        merged_list = self.merge(range_list, s, length)
        max_len = 0
        for interval in merged_list:
            tmp = interval[1] - interval[0] + 1
            max_len = tmp if tmp > max_len else max_len
        return max_len

    def merge(self, range_list, s, length):
        merge_flag = False
        for interval in range_list:
            while ((interval[0] - 1 >= 0 and interval[1] + 1 < length)
                   and (s[interval[0] - 1] == self.l and s[interval[1] + 1] == self.r)):
                merge_flag = True
                interval[0] -= 1
                interval[1] += 1
        if not merge_flag:
            return range_list
        rst_list = []
        for i in range(len(range_list) - 1):
            if range_list[i][1] + 1 == range_list[i + 1][0]:
                range_list[i + 1][0] = range_list[i][0]
            else:
                rst_list.append(range_list[i])
        rst_list.append(range_list[-1])
        return self.merge(rst_list, s, length)

s = Solution()
t1 = "(()"
print(s.longestValidParentheses(t1))
t2 = ")()())"
print(s.longestValidParentheses(t2))
t3 = ")()))(())"
print(s.longestValidParentheses(t3))
t4 = ")((()()))()()((())())"
print(s.longestValidParentheses(t4))
