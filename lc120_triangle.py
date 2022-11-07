'''
120. Triangle
Medium

1457

171

Favorite

Share
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
'''


class Solution:
    def minimumTotal(self, triangle) -> int:
        '''From down to up
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]
        '''

        '''From up to down
        '''
        if len(triangle) == 1:
            return triangle[0][0]

        for i in range(1, len(triangle)):
            triangle[i][0] += triangle[i - 1][0]
            for j in range(1, i):
                triangle[i][j] += min(triangle[i - 1][j - 1],
                                      triangle[i - 1][j])
            triangle[i][-1] += triangle[i - 1][-1]
        return min(triangle[i])

t1 = [
    [2]
]
print(Solution().minimumTotal(t1))
t2 = [
    [2],
    [3, 4]
]
print(Solution().minimumTotal(t2))
t3 = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]
print(Solution().minimumTotal(t3))

