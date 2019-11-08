'''面试题22：链表中倒数第k个节点

输入一个链表，输出该链表中倒数第k个节点。从1开始计数，即链表的尾节点是倒数第1个节点。
---------------
Example
input:1-2-3-4-5-6, 3
output:4
-------------------
当我们用一个指针遍历链表不能解决问题的时候，可以尝试用两个指针来遍历链表。
可以让其中一个指针遍历的速度快一些（比如一次在链表上走两步），或者让它先在链表上走若干步。
'''
class Node(object):

    def __init__(self, value=None, next_node= None):
        self.value = value
        self.next = next_node

def find_k_to_tail(head, k):

    if head is None or k < 1:
        return None

    front = head

    for _ in range(k-1):
        if front.next is not None:
            front = front.next
        else:
            return None
    
    cur = head
    while front.next is not None:
        cur = cur.next
        front = front.next

    return cur.value

def __linked_list(arr):

    cur = head = Node()

    for x in arr:
        cur.next = Node(x)
        cur = cur.next
    cur = head
    head = head.next
    cur.next = None
    return head
    
if __name__ == "__main__":

    k = [0,1,3,5,6]
    data1 = [1, 2, 3, 4, 5]
    for kth in k:
        print(find_k_to_tail(__linked_list(data1),kth))
    