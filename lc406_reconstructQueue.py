'''406. 根据身高重建队列
假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来重建这个队列。

注意：
总人数少于1100人。

示例

输入:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

输出:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
'''
class Solution:
    def reconstructQueue(self, people: list) -> list:
        people.sort(key=lambda x: (-x[1]))
        rst = list()
        for p in people:
            rst.insert(p[1], p)
        return rst

    def reconstructQueueSelf(self, people: list) -> list:
        if len(people) < 2:
            return people
        people.sort(key=lambda x:(x[1], x[0]), reverse=True)
        rst = [people.pop()]
        while people:
            cur = people.pop()
            num, cnt = cur
            for i in range(len(rst)):
                if rst[i][0] >= num:
                    cnt -= 1
                if cnt == 0:
                    cur_i = i + 1
                    while cur_i < len(rst):
                        if rst[cur_i][0] >= num:
                            break
                        cur_i += 1
                    rst.insert(cur_i, cur)
                    break
            else:
                rst.append(cur)
        return rst


s = Solution()
t1 = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(s.reconstructQueue(t1))

print([0] * 26)