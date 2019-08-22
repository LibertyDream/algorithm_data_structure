from collections import deque
from enum import Enum, unique


class Node(object):
    def __init__(self, ele, left = None, right = None):
        self.ele = ele
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.ele)

# 用于模仿系统栈进行非递归遍历时的命令类
@unique
class Command(Enum):
    VISIT = 'visit'
    GOTO = 'goto'


class BST(object):
    def __init__(self):
        self.__root = None
        self.__size = 0

    #  返回二分搜索树大小
    def get_size(self):
        return self.__size

    #  判断二分搜索树是否为空
    def is_empty(self):
        return self.__size == 0

    #  向二分搜索树添加一个新元素ele
    def add(self, ele):
        self.__root = self.__add_recur(self.__root, ele)

    #  向以node为根的二分搜索树添加新元素ele，递归实现
    #  不接受重复元素，返回添加新元素后的根节点
    def __add_recur(self, node: Node, ele):

        if node is None:
            self.__size += 1
            return Node(ele)

        if ele > node.ele:
            node.right = self.__add_recur(node.right, ele)
        if ele < node.ele:
            node.left = self.__add_recur(node.left, ele)

        return node

    #  向以node为根的二分搜索树添加新元素ele，非递归实现
    #  不接受重复元素，返回添加新元素后的根节点
    def __add_non_recur(self, node: Node, ele):

        direction = -1  # 标识前进方向，-1：没动，1：向左，0：向右
        pre = node  # node所在的前一个位置
        root = node  # 记录传入的根节点，也是返回值

        while True:
            if node is None:
                if direction == -1:
                    root = Node(ele)

                if direction == 1:
                    pre.left = Node(ele)

                if direction == 0:
                    pre.right = Node(ele)

                self.__size += 1
                return root

            if ele > node.ele:
                pre = node
                node = node.right
                direction = 0
            elif ele < node.ele:
                pre = node
                node = node.left
                direction = 1
            else:
                return root

    #  二分搜索树是否包含元素ele，返回布尔值
    def contains(self, ele):
        return self.__contains_non_recur(self.__root, ele)

    #  以node为根的二分搜索树是否包含元素ele，返回布尔值，递归实现
    def __contains_recur(self, node: Node, ele):
        if node is None:
            return False

        if ele > node.ele:
            return self.__contains_recur(node.right, ele)
        elif ele < node.ele:
            return self.__contains_recur(node.left, ele)
        else:  # ele == node.ele
            return True

    #  以node为根的二分搜索树是否包含元素ele，返回布尔值，非递归实现
    def __contains_non_recur(self, node: Node, ele):

        while True:
            if node is None:
                return False

            if ele > node.ele:
                node = node.right
            elif ele < node.ele:
                node = node.left
            else:  # ele == node.ele
                return True

    #  前序遍历
    def pre_order(self):
        self.__pre_order_non_recur_book(self.__root)

    #  中序遍历
    def in_order(self):
        self.__in_order_non_recur_book(self.__root)

    #  后序遍历
    def post_order(self):
        self.__post_order_non_recur_book(self.__root)

    #  前序遍历以node为根节点的二分搜索树，递归实现
    def __pre_order_recur(self, node: Node):

        if node is None:
            return

        print(node.ele, end=' ')

        if node.left is not None:
            self.__pre_order_recur(node.left)
        if node.right is not None:
            self.__pre_order_recur(node.right)

    #  中序遍历以node为根节点的二分搜索树，递归实现
    def __in_order_recur(self, node: Node):

        if node is None:
            return

        if node.left is not None:
            self.__in_order_recur(node.left)

        print(node.ele, end=' ')

        if node.right is not None:
            self.__in_order_recur(node.right)

    #  后序遍历以node为根的二分搜索树，递归实现
    def __post_order_recur(self, node: Node):

        if node is None:
            return

        if node.left is not None:
            self.__post_order_recur(node.left)
        if node.right is not None:
            self.__post_order_recur(node.right)

        print(node.ele, end=' ')

    #  前序遍历以node为根节点的二分搜索树，模仿系统栈的非递归实现
    #  python list 作为栈使用时结构为
    #  [1,2,3,4] top
    def __pre_order_non_recur(self, node: Node):

        stack = []

        if node is not None:
            stack.append({Command.GOTO: node})
        while len(stack) > 0:
            command, cur = stack.pop().popitem()

            if command == Command.VISIT:
                print(cur.ele, end=' ')
            else:  # command == Command.GOTO

                #  栈结构，注意命令入栈顺序

                if cur.right is not None:
                    stack.append({Command.GOTO: cur.right})
                if cur.left is not None:
                    stack.append({Command.GOTO: cur.left})
                stack.append({Command.VISIT: cur})

    #  中序遍历以node为根的二分搜索树，模仿系统栈的非递归实现
    def __in_order_non_recur(self, node: Node):
        stack = []
        if node is not None:
            stack.append({Command.GOTO: node})
        while len(stack) > 0:
            command, cur = stack.pop().popitem()

            if command == Command.VISIT:
                print(cur.ele, end=' ')
            else:  # command == Command.GOTO
                if cur.right is not None:
                    stack.append({Command.GOTO: cur.right})
                stack.append({Command.VISIT: cur})
                if cur.left is not None:
                    stack.append({Command.GOTO: cur.left})

    #  后序遍历以node为根的二分搜索树，模仿系统栈的非递归实现
    def __post_order_non_recur(self, node: Node):
        stack = []
        if node is not None:
            stack.append({Command.GOTO: node})
        while len(stack) > 0:
            command, cur = stack.pop().popitem()

            if command == Command.VISIT:
                print(cur.ele, end=' ')
            else:  # command == Command.GOTO
                stack.append({Command.VISIT: cur})
                if cur.right is not None:
                    stack.append({Command.GOTO: cur.right})
                if cur.left is not None:
                    stack.append({Command.GOTO: cur.left})

    #  前序遍历以node为根节点的二分搜索树，教科书式非递归实现
    def __pre_order_non_recur_book(self, node: Node):

        stack = []
        cur = node
        while cur is not None or len(stack) > 0:
            while cur is not None:
                print(cur.ele, end=' ')

                stack.append(cur)
                cur = cur.left

            if len(stack) > 0:
                cur = stack.pop()
                cur = cur.right

    #  中序遍历以node为根节点的二分搜索树，教科书式非递归实现
    def __in_order_non_recur_book(self, node: Node):

        stack = []
        cur = node
        while cur is not None or len(stack) > 0:
            while cur is not None:
                stack.append(cur)
                cur = cur.left

            if len(stack) > 0:
                cur = stack.pop()
                print(cur.ele, end=' ')
                cur = cur.right

    #  后序遍历以node为根节点的二分搜索树，教科书式非递归实现
    def __post_order_non_recur_book(self, node: Node):

        stack = []
        pre = cur = node
        while cur is not None or len(stack) > 0:
            while cur is not None:
                stack.append(cur)
                cur = cur.left

            if len(stack) > 0:
                cur = stack.pop()

                if cur.right is not None and pre != cur.right:
                    stack.append(cur)
                    cur = cur.right
                else:
                    print(cur.ele, end=' ')
                    pre = cur
                    cur = None

    #  层序遍历
    def level_order(self):
        self.__level_order(self.__root)

    #  层序遍历以node为根节点的二分搜索树
    def __level_order(self, node: Node):
        queue = deque()

        if node is not None:
            queue.append(node)
        while len(queue) > 0:
            cur = queue.popleft()

            print(cur.ele, end=' ')

            if cur.left is not None:
                queue.append(cur.left)
            if cur.right is not None:
                queue.append(cur.right)

    #  返回二分搜索树的最大值
    def max(self):
        if self.__size == 0:
            raise AttributeError('BST is empty!')
        return self.__max(self.__root).ele

    #  返回以node为根的二分搜索树的最大值所在节点
    def __max(self, node: Node):

        if node.right is None:
            return node

        return self.__max(node.right)

    #  返回二分搜索树的最小值
    def min(self):
        if self.__size == 0:
            raise AttributeError('BST is empty!')
        return self.__min(self.__root).ele

    #  返回以node为根的二分搜索树的最小值所在的节点
    def __min(self, node: Node):

        if node.left is None:
            return node

        return self.__min(node.left)

    #  删除并返回最小值
    def remove_min(self):
        ret = self.min()
        self.__root = self.__remove_min(self.__root)
        return ret

    #  从以node为根的二分搜索树中删除最小值，并返回删除后的根节点
    def __remove_min(self, node: Node):

        if node.left is not None:
            node.left = self.__remove_min(node.left)
            return node

        self.__size -= 1
        ret = node.right
        node.right = None
        return ret

    #  删除并返回最大值
    def remove_max(self):
        ret = self.max()
        self.__root = self.__remove_max(self.__root)
        return ret

    #  从node为根节点的二分搜索树中删除最大值，并返回删除后的根节点
    def __remove_max(self, node: Node):

        if node.right is not None:
            node.right = self.__remove_max(node.right)
            return node

        self.__size -= 1
        ret = node.right
        node.right = None
        return ret

    #  删除元素ele
    def remove_ele(self, ele):
        if self.__size == 0:
            raise AttributeError('BST is empty!')
        self.__root = self.__remove_ele(self.__root, ele)

    #  从以node为根的二分搜索树中删除元素ele,并返回删除元素后的根节点
    def __remove_ele(self, node: Node, ele) -> Node:

        ret = node

        if node is None:
            return ret

        if ele > node.ele:
            node.right = self.__remove_ele(node.right, ele)
        elif ele < node.ele:
            node.left = self.__remove_ele(node.left, ele)
        else:  # ele == node.ele
            if node.left is None:
                ret = node.right
                node.right = None
                self.__size -= 1
            elif node.right is None:
                ret = node.left
                node.left = None
                self.__size -= 1
            else:  # 左右子树皆不为空，可以选择左子树的最大值或右子树的最小值为新的根
                ret = self.__min(node.right)
                ret.right = self.__remove_min(node.right)  # 注意赋值顺序，先右再左
                ret.left = node.left
                node.left = None
                node.right = None

        return ret


    def __str__(self):
        b_str = ''
        return self.__gen_bst_str(self.__root, 0, b_str)

    def __gen_bst_str(self, node: Node, depth: int, b_str: str):

        if node is None:
            b_str += 'null'
            return b_str

        b_str += '--' * depth + str(node) + '\n'

        if node.left is not None:
            b_str += self.__gen_bst_str(node.left, depth+1, '')

        if node.right is not None:
            b_str += self.__gen_bst_str(node.right, depth+1, '')

        return b_str
