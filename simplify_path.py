def simplify_path(path):


# 验证学生答案的示例
def validate_student_answer():
    # 验证路径简化
    assert simplify_path("/home/") == "/home"
    assert simplify_path("/a/./b/../../c/") == "/c"
    assert simplify_path("/a//b////c/d//././/..") == "/a/b/c"

    print("学生答案通过验证。")

# 运行验证函数
validate_student_answer()
