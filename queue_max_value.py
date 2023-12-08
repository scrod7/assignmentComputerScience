class MaxQueue:
    def __init__(self):
        self.value_queue = list()
        self.max_element_queue = list()

    def push(self, value):
        self.value_queue.append(value)
        while self.max_element_queue and value > self.max_element_queue[-1]:
            self.max_element_queue.pop()
        self.max_element_queue.append(value)

    def pop(self):
        if not self.value_queue:
            return -1
        pop_value = self.value_queue.pop()
        if pop_value == self.max_element_queue[0]:
            self.max_element_queue.pop()
        return pop_value

    def max_value(self):
        return -1 if not self.max_element_queue else self.max_element_queue[0]

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