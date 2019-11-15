'''面试题52：两个链表的第一个公共节点

输入两个链表，找出它们的第一个公共节点
'''

class Node(object):
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

def find_first_common_node(head_1, head_2):

    if head_1 is None or head_2 is None:
        return None

    len_1 = __get_len(head_1)
    len_2 = __get_len(head_2)
    dif = len_1 - len_2

    long_list = head_1 
    short_list = head_2

    if dif < 0:
        dif = len_2 - len_1
        long_list = head_2
        short_list = head_1
    
    for _ in range(dif):
        long_list = long_list.next_node

    while long_list is not None and short_list is not None and long_list != short_list:
        long_list = long_list.next_node
        short_list = short_list.next_node
    
    return long_list


def __get_len(head):

    if head is None:
        return 0

    count = 0
    cur = head
    while cur is not None:
        cur = cur.next_node
        count += 1

    return count