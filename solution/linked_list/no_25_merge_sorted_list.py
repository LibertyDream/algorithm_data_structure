'''面试题25：合并两个排序的链表

输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的
-----------------
Example
input:1-3-5-7, 2-4-6-8
output:1-2-3-4-5-6-7-8
'''

class Node(object):

    def __init__(self, value=None, next_node= None):
        self.value = value
        self.next_node = next_node

def __linked_list(arr):

    if arr is None:
        return None
    cur = head = Node()

    for x in arr:
        cur.next_node = Node(x)
        cur = cur.next_node
    cur = head
    head = head.next_node
    cur.next_node = None
    return head

def merge_sorted_linked_list(head_1, head_2):
    if head_1 is None or head_2 is None:
        return head_2 if head_1 is None else head_1

    new_head = None

    if head_1.value < head_2.value:
        new_head = head_1
        new_head.next_node = merge_sorted_linked_list(head_1.next_node, head_2)
    else:
        new_head = head_2
        new_head.next_node = merge_sorted_linked_list(head_1, head_2.next_node)

    return new_head

def __str_linked_list(head):
    if head is None:
        return 'None'
    ret = ''
    cur = head
    while cur is not None:
        ret = ret + str(cur.value)
        if cur.next_node is not None:
            ret += '->'
        cur = cur.next_node
    return ret

if __name__ == "__main__":

    data1 = [[1,3,5,7],[2,4,6,8]]
    data2 = [None, [1,2,3]]
    data3 = [[3,4,5],None]
    data4 = [[2],[1]]

    datas = [data1, data2, data3,data4]

    for data in datas:
        x, y = data
        head_1 = __linked_list(x)
        head_2 = __linked_list(y)
        print(__str_linked_list(head_1), __str_linked_list(head_2),
        __str_linked_list(merge_sorted_linked_list(head_1, head_2)))
