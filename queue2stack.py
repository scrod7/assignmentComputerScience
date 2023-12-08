class MyStack:
    def __init__(self):
        self.queue = list()

    def push(self, x):

    def pop(self):

    def peak(self):

    def empty(self):


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