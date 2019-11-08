'''面试题24：反转链表

定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
'''
class Node(object):

    def __init__(self, value=None, next_node= None):
        self.value = value
        self.next = next_node

    def __str__(self):

        return str(self.value)

def __linked_list(arr):

    cur = head = Node()

    for x in arr:
        cur.next = Node(x)
        cur = cur.next
    cur = head
    head = head.next
    cur.next = None
    return head

def reverse_linked_list(head):

    if head is None:
        return None

    new_head = pre = None

    cur = head
    while cur is not None:

        next_node = cur.next

        if next_node is None:
            new_head = cur
        
        cur.next = pre
        pre = cur
        cur = next_node
    
    return new_head

if __name__ == "__main__":

    data1 = [1, 2, 3, 4, 5]
    data2 = [1]
    lt = __linked_list(data2)
    while lt is not None:
        print(lt, end=' ')
        lt = lt.next
    print('|',end=' ')
    lt = reverse_linked_list(__linked_list(data2))
    while lt is not None:
        print(lt, end=' ')
        lt = lt.next