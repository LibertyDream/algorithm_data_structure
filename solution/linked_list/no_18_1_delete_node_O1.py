'''面试题18-1：删除链表的节点

在O（1）时间内删除链表节点。给定单向链表的头指针和一个节点指针，
定义一个函数在O（1）时间内删除该节点
'''

'''
class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
'''

def delete_node(head, node):
    
    if head is None or node is None:
        raise Exception('head or node is None')

    if node.next is not None:
        latter = node.next
        node.value = latter.value
        node.next = latter.next
        latter.next = None
    elif head == node: # 只有一个头结点
        head = None
        node = None
    else: # 尾结点
        cur = head
        while cur.next != node:
            cur = cur.next
        cur.next = None
        node = None