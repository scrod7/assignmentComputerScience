from collections import deque


class MaxQueue:
    def __init__(self):
        self.queue = deque()

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        self.queue.pop()

    def max_value(self):
        return max(self.queue)

def validate_student_answer():
    # 创建 MaxQueue 实例
    max_queue = MaxQueue()

    # 验证 push 和 max_value 方法
    max_queue.push(1)
    assert max_queue.max_value() == 1
    max_queue.push(3)
    assert max_queue.max_value() == 3
    max_queue.push(2)
    assert max_queue.max_value() == 3

    # 验证 pop 方法
    assert max_queue.pop() == 1
    assert max_queue.max_value() == 3
    assert max_queue.pop() == 3
    assert max_queue.max_value() == 2

    print("答案通过验证。")


# 运行验证函数
validate_student_answer()