from collections import deque

class MaxQueue:
    def __init__(self):
        self.queue = deque()
        self.max_queue = deque()

    def push(self, value):
        q, mq = self.queue, self.max_queue
        q.append(value)
        while mq and value > mq[-1]: mq.pop()
        mq.append(value)

    def pop(self):
        q, mq = self.queue, self.max_queue
        if not q: return None
        if q[0] == mq[0]: mq.popleft()
        return q.popleft()

    def max_value(self):
        return self.max_queue[0] if self.max_queue else -1

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