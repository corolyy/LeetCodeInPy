"""
回溯框架

result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return

    for 选择 in 选择列表:
        做选择
        backtrace(路径', 选择列表')
        撤销选择
"""