from collections import deque
class MyStack:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x):
        self.queue1.append(x)

    def pop(self):
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        result = self.queue1.popleft()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return result

    def top(self):
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        result = self.queue1[0]
        self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1
        return result

    def empty(self):
        return len(self.queue1) == 0 and len(self.queue2) == 0



# 验证用的代码：
def validate_student_answer():
    # 创建 MyStack 实例
    my_stack = MyStack()

    # 验证 push、pop、peak 和 empty 方法
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    assert my_stack.peak() == 3
    assert my_stack.pop() == 3
    assert my_stack.pop() == 2
    assert not my_stack.empty()

    print("答案通过验证。")


# 运行验证函数
validate_student_answer()