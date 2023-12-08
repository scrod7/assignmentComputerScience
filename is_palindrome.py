class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def is_palindrome_linked_list(head):
    node_now = ListNode()
    his = ""
    while node_now.next != None:
        his += str(node_now.value)
        node_now = node_now.next
    return his == his[::-1]


def validate_student_answer():
    # 创建链表 1 -> 2 -> 2 -> 1
    head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))

    # 验证 is_palindrome_linked_list 方法
    assert is_palindrome_linked_list(head)

    # 创建链表 1 -> 2 -> 3 -> 4
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

    # 验证 is_palindrome_linked_list 方法
    assert not is_palindrome_linked_list(head)

    print("答案通过验证。")

# 运行验证函数
validate_student_answer()