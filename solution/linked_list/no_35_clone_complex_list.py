'''面试题35：复杂链表的复制

请实现函数 clone(node:ComplexNode)，复制一个复杂链表。在复杂链表中，
每个节点除了有一个m pNext 指针指向下一个节点，还有一个mpSibling指针指向链表中的任意节点
或者nullptr
'''

class ComplexNode(object):

    def __init__(self, value=None, next_node=None, other=None):
        self.value = value
        self.next = next_node
        self.other = other

def clone(node:ComplexNode):
    if node is None:
        return None

    __duplicate(node)
    __link(node)
    return __split(node)

def __duplicate(head:ComplexNode):

    cur = head
    while cur is not None:
        clone_node = ComplexNode()
        clone_node.value = cur.value
        clone_node.next = cur.next
        
        cur.next = clone_node
        cur = clone_node.next

def __link(head:ComplexNode):
    
    cur = head

    while cur is not None:
        clone_node = cur.next
        if cur.other is not None:
            clone_node.other = cur.other.next
        
        cur = clone_node.next
        

def __split(head:ComplexNode):
    
    clone_head = head.next

    cur = head
    clone_node = cur.next
    cur.next = clone_node.next
    cur = clone_node.next

    while cur is not None:
        clone_node.next = cur.next
        clone_node = cur.next
        cur.next = clone_node.next
        cur = cur.next
    
    return clone_head
        