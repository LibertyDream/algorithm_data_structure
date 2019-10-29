'''面试题6：从尾到头打印链表

输入一个链表的头节点，从尾到头反过来打印出每个节点的值。
----------------
Example
input: 1->5->3->4
output:4351
----------------------
如果要修改输入数据要询问（逆转链表），观测输入输出顺序考虑特殊辅助结构，栈、递归和循环间的关系
'''
class Node(object):

    def __init__(self, value=None, next_node = None):
        self.value = value
        self.next_node = next_node

def print_list_reversely(head):
    if head is None:
        return

    cur = head
    temp = []
    while cur is not None:
        temp.append(cur.value)
        cur = cur.next_node

    for i in range(len(temp)):
        print(temp.pop(),end=' ')
    print()

def __init_list(arr):

    cur = head = None
    for x in arr:
        if cur is None:
            cur = head = Node(x)
        else:
            cur.next_node = Node(x)
            cur = cur.next_node
    return head
            
if __name__ == "__main__":

    data1 = [1,2,3,4,5]
    data2 = [1]

    link_list1 = __init_list(data1)
    link_list2 = __init_list(data2)

    print_list_reversely(None)
    print_list_reversely(link_list1)
    print_list_reversely(link_list2)

