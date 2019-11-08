'''面试题23：链表中环的入口节点

如果一个链表中包含环，如何找出环的入口节点
-------------
Example
    _______
    |     | 
1-2-3-4-5-6

output:3
'''

class Node(object):

    def __init__(self, value=None, next_node= None):
        self.value = value
        self.next = next_node

    def __str__(self):

        return 'value: %s, next: %s' % (str(self.value), str(self.next.value if self.next is not None else None))
        
def __meet_node(head):

    if head is None:
        return None

    fast = head.next
    slow = head
    while fast is not None and slow is not None:

        if fast == slow:
            return slow
        
        slow = slow.next
        fast = fast.next
        if fast is not None:
            fast = fast.next
    
    return None

def entry_of_loop(head):

    meet = __meet_node(head)

    if meet is None:
        return None

    loop_size = 1
    cur = meet.next
    while cur != meet:
        loop_size += 1
        cur = cur.next
    
    front = cur = head

    for _ in range(loop_size - 1):
        front = front.next
    
    while front.next != cur:
        cur = cur.next
        front = front.next
    
    return cur

def __loop_linked_list(arr, loop_size):

    entry = cur = head = Node()
    count = 0
    for x in arr:
        count += 1
        cur.next = Node(x)
        cur = cur.next
        if loop_size > 0 and count >= loop_size:
            entry = entry.next
    
    cur.next = entry

    cur = head
    head = head.next
    cur.next = None
    return head

if __name__ == "__main__":

    loop_size = [0,1,2,3,4,5]
    data1 = [1, 2, 3, 4, 5]

    for loop in loop_size:
        print(entry_of_loop(__loop_linked_list(data1,loop)))


