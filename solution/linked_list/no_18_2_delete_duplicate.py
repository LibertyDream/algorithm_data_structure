'''面试题18-2：删除链表中重复的节点。

在一个排序的链表中，删除重复的节点
----------
Example
input:1-2-3-3-4-4-5
output:1-2-5
'''

'''
class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
'''

def delete_duplicates(head):

    if head is None:
        raise Exception('head is None')

    cur = head
    pre = None
    while cur is not None:
        need_delete = False
        next_node = cur.next
        if next_node is not None and next_node.value == cur.value:
            need_delete = True
        
        if not need_delete:
            pre = cur
            cur = cur.next
        else:
            value = cur.value
            while cur is not None and cur.value == value:
                next_node = cur.next
                cur = None
                cur = next_node
            if pre is None:
                head = next_node
            else:
                pre.next = next_node